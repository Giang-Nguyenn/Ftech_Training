import base64
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


from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from django.contrib.auth.models import User
from .models import Projects, Task, UserProject
from .permissions import IsUserInProjectPermisson

from .serializers import (UserReadOnlySerializer,
                          UserSerializers,
                          ProjectSerializers,
                          TaskSerializers,
                          TaskSerializers1,
                          TaskSerializers2,
                          TaskPostSerializers,
                          ProjectUpdateUserSerializers,
                          ProjectListUserSerializers,
                          ProjectReadOnlySerializer,
                          )
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
            # return self.permission_view_class[self.action]
        return [permission() for permission in self.permission_classes]

# ____________View____________-


class Project(GetPermissionMixin, GetSerializerMixin, ModelViewSet):
    queryset = Projects.objects.all()  # select_related, prefetch_related

    serializer_class = ProjectSerializers
    serializer_view_class = {
        "list": ProjectReadOnlySerializer,
        "retrieve": ProjectReadOnlySerializer
    }

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    permission_view_class = {
        'list': [IsAuthenticated],
        'retrieve': [IsUserInProjectPermisson],
        # 'update': [IsAdminUser],
        # 'partial_update': [IsAdminUser],
        # 'create': [IsAdminUser],
        # 'destroy': [IsAdminUser]
    }

    def list(self, request, *args, **kwargs):
        print(request.user)
        if(request.user.is_staff):
            queryset = Projects.objects.all()
        else:
            queryset = request.user.projects_set.all()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Task(ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializers1
    pagination_class = PageNumberPagination


class ProjectListUser(GetPermissionMixin, GetSerializerMixin, ModelViewSet):
    serializer_class = UserSerializers
    serializer_view_class = {
        "list": UserReadOnlySerializer,
        'create': ProjectUpdateUserSerializers
    }
    authentication_classes = [BasicAuthentication]

    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_view_class = {
        'list': [IsAuthenticated],
        'create': [IsAdminUser],
        'destroy': [IsAdminUser]
    }

    def get_queryset(self):
        pro = Projects.objects.get(pk=self.request.GET['pk'])
        queryset = pro.members.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = ProjectUpdateUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_id = serializer.data['id']
        UserProject.objects.create(project=Projects.objects.get(pk=self.request.GET['pk']),
                                   user=User.objects.get(pk=user_id)
                                   )
        return Response('Thành công', status=status.HTTP_201_CREATED,)


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
            # 'email': user.email
        })


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
