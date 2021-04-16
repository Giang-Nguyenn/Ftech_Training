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

from django.contrib.auth.models import User
from .models import Projects, Task, UserProject

from .serializers import (UserSerializers,
                          ProjectSerializers,
                          TaskSerializers,
                          TaskSerializers1,
                          TaskSerializers2,
                          TaskPostSerializers,
                          ProjectAddUserSerializers,
                          ProjectListUserSerializers,
                          ProjectReadOnlySerializer)


class GetSerializerMixin:
    serializer_view_class = {}

    def get_serializer_class(self):
        if self.action in self.serializer_view_class:
            return self.serializer_view_class[self.action]
        return self.serializer_class


# Create your views here.
class Project(GetSerializerMixin, ModelViewSet):
    queryset = Projects.objects.all()  # select_related, prefetch_related
    serializer_class = ProjectSerializers
    serializer_view_class = {
        "list": ProjectReadOnlySerializer,
        "retrieve": ProjectReadOnlySerializer
    }


class Task(ModelViewSet):
    queryset = Task.objects.all()
    # serializer_class = TaskSerializers
    serializer_class = TaskSerializers1

    # def get_serializer_class(self):
    #     if self.request.method == "POST":
    #         return TaskPostSerializers
    #     return TaskSerializers


class ProjectListUser(ModelViewSet):
    # queryset=UserProject.objects.all()
    # serializer_class=ProjectListUserSerializers

    # serializer_class=UserSerializers

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ProjectAddUserSerializers
        return UserSerializers

    def get_queryset(self):
        # print(type(self.request.data))
        print(self.request.GET['pk'])
        pro = Projects.objects.get(pk=self.request.GET['pk'])
        queryset = pro.members.all()
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = ProjectAddUserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print(type(serializer.data['username']))
        user = serializer.data['username']
        # user=User.objects.get(username=serializer.data['username'])
        # print(user)

        UserProject.objects.create(project=Projects.objects.get(pk=self.request.GET['pk']),
                                   user=User.objects.get(pk=user.id)
                                   )
        return Response('Thành công', status=status.HTTP_201_CREATED,)


def test(request):
    return HttpResponse('test')
