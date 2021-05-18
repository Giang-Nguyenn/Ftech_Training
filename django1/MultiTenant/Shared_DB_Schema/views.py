import base64
from django.db.models.query import QuerySet
from django.db.utils import Error
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from django.shortcuts import redirect
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.db import transaction, DatabaseError
from django.conf import global_settings
from safedelete import config


from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser,
                                        )
from django.contrib.auth.models import User
from .models import Projects, Task, UserProject, User, Tenant

from .permissions import (IsUserInProjectPermisson,
                          UserInProjectPermisson,
                          IsSuperAdmin)
                          
from django_filters.rest_framework import DjangoFilterBackend
from .filters import UserFilter, ProjectFilter,TaskFilter

from .serializers import (UserReadOnlySerializer,
                          SuperUserSerializers,
                          UserSerializers,
                          ProjectSerializers,
                          TaskSerializers,
                          TaskPostSerializers,
                          ProjectUpdateUserSerializers,
                          ProjectListUserSerializers,
                          ProjectReadOnlySerializer,
                          TenantSerializers,
                          TenantSerializersAll,
                          UserReadOnlySerializerAll,
                          SuperUserSerializersAll,
                          )
                          
from .utils import tenant_from_request

from safedelete.models import SafeDeleteModel
# Create your views here.

# _______class Mixin_____________


class GetSerializerMixin:
    serializer_view_class = {}

    def get_serializer_class(self):
        if self.action in self.serializer_view_class:
            return self.serializer_view_class[self.action]
        return self.serializer_class


class GetPermissionMixin:
    permission_view_class = {}

    def get_permissions(self):
        if self.action in self.permission_view_class:
            return [permission() for permission in self.permission_view_class[self.action]]
        return [permission() for permission in self.permission_classes]


class ModelViewSetCustom(ModelViewSet):
    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        # print(tenant)
        return super().get_queryset().filter(tenant=tenant)

    def create(self, request, *args, **kwargs):
        ten = tenant_from_request(request).id
        request.data.update({'tenant': ten})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)


# ____________View____________-


class TenantView(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializers
    filter_backends = [DjangoFilterBackend]
    # filter_class = ProjectFilter
    permission_classes = [IsSuperAdmin]


class CreateSuperUser(ModelViewSet):
    queryset=User.objects.filter(is_staff=True)
    serializer_class=SuperUserSerializers
    permission_classes=[IsSuperAdmin]

    def create(self, request, *args, **kwargs):
        request.data.update({'is_staff':True,'is_superuser':True})
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class Project(GetPermissionMixin, GetSerializerMixin, ModelViewSetCustom):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializers
    filter_backends = [DjangoFilterBackend]
    filter_class = ProjectFilter
    # filterset_fields = ['members__id']
    serializer_view_class = {
        "list": ProjectReadOnlySerializer,
        "retrieve": ProjectReadOnlySerializer
    }

    permission_classes = [IsAdminUser]
    permission_view_class = {
        'list': [IsAuthenticated],
        'retrieve': [IsUserInProjectPermisson],
    }




class Task(ModelViewSetCustom):
    # permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    filter_backends = [DjangoFilterBackend]
    filter_class = TaskFilter
    pagination_class = PageNumberPagination


class Users(GetPermissionMixin, GetSerializerMixin, ModelViewSetCustom):
    queryset = User.objects.all()
    # authentication_classes = [BasicAuthentication]
    filter_backends = [DjangoFilterBackend]
    filter_class = UserFilter
    serializer_class = UserSerializers
    serializer_view_class = {
        "list": UserReadOnlySerializer,
        "retrieve": UserReadOnlySerializer
    }
    permission_classes = [IsAdminUser]
    permission_view_class = {
        'list': [IsAuthenticated],
    }



class ProjectListUser(GetPermissionMixin, GetSerializerMixin, ModelViewSet):
    serializer_class = UserSerializers
    serializer_view_class = {
        "list": UserReadOnlySerializer,
        'create': ProjectUpdateUserSerializers
    }

    permission_classes = [IsUserInProjectPermisson]
    permission_view_class = {
        'list': [UserInProjectPermisson, ]
    }

    def get_object(self):
        obj = Projects.objects.filter(pk=self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_queryset(self):
        ten = tenant_from_request(self.request)
        # queryset = pro.members.filter(tenant=ten)
        pro = Projects.objects.filter(tenant=ten).prefetch_related(
            'members').filter(pk=self.kwargs['pk']).first()
        queryset = pro.members.all()
        return queryset

    def create(self, request, *args, **kwargs):
        '''
        data={'id':'1,2,3...'}
        '''
        serializer = ProjectUpdateUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data['id']
        list_user_id = user_id.split(',')
        number = 0
        ten=tenant_from_request(request)
        try:
            with transaction.atomic():
                for id in list_user_id:
                    number = number+1
                    print(number)
                    user_p = UserProject.objects.filter(project=Projects.objects.get(pk=self.kwargs['pk']),
                                                        user=User.objects.get(pk=id),
                                                        tenant=ten)
                    if not user_p:
                        UserProject.objects.create(project=Projects.objects.get(pk=self.kwargs['pk']),
                                                   user=User.objects.get(pk=id),
                                                   tenant=ten)
                    if number == 3: # test atomic
                        print('lỗi')
                        UserProject.objects.createe(project=Projects.objects.get(pk=self.kwargs['pk']),
                                                    user=User.objects.get(pk=id))
        except:
            return Response('Error')
        return Response('Thành công', status=status.HTTP_201_CREATED,)

    def destroy(self, request, *args, **kwargs):
        """
        request.data['id']="1,2,3,4,5"
        """
        serializer = ProjectUpdateUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data['id']
        list_user_destroy = user_id.split(',')
        print(list_user_destroy)
        ten=tenant_from_request(request)
        query = UserProject.objects.filter(project=Projects.objects.get(pk=self.kwargs['pk']),
                                           user__id__in=list_user_destroy,
                                           tenant=ten)
        print(query)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ____Safedelete____

class TenantAll(ModelViewSet):
    queryset = Tenant.all_objects.all()
    serializer_class = TenantSerializersAll
    permission_classes = [IsSuperAdmin]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.get('deleted') =='False':
            instance.undelete()
            return Response('undelete %s thành công'%instance )
        return Response(request.data)

class UserAll(ModelViewSetCustom):
    queryset = User.all_objects.all()
    serializer_class = UserReadOnlySerializerAll
    permission_classes = [IsAdminUser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.get('deleted') =='False':
            instance.undelete()
            return Response('undelete %s thành công'%instance )
        return Response(request.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete(force_policy=config.HARD_DELETE)
        return Response('Xoá thành công',status=status.HTTP_204_NO_CONTENT)

class SuperUserAll(ModelViewSet):
    queryset=User.all_objects.filter(is_staff=True)
    serializer_class=SuperUserSerializersAll
    permission_classes=[IsSuperAdmin]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.get('deleted') =='False':
            instance.undelete()
            return Response('undelete %s thành công'%instance )
        return Response(request.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete(force_policy=config.HARD_DELETE)
        return Response('Xoá thành công',status=status.HTTP_204_NO_CONTENT)



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })

from safedelete.admin import SafeDeleteAdmin, highlight_deleted

# ---------------Test---------------


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


HTTP_HEADER_ENCODING = 'iso-8859-1'


def test(request):
    auth = get_authorization_header(request).split()
    # auth_decoded = base64.b64decode(auth[1]).decode('utf-8')
    # auth_parts = auth_decoded.partition(':')
    # return HttpResponse('%s---%s' % (auth_decoded, auth_parts))
    return HttpResponse('%s' % request.META)
    # return HttpResponse('test method là : %s' % (request.method))
