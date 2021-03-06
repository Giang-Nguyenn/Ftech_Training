from django_filters import rest_framework as filters
from rest_framework.fields import Field
# from django.contrib.auth.models import User

from .models import Projects,User,Task


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='exact')
    username__iexact = filters.CharFilter(
        field_name='username', lookup_expr='iexact')

    class Meta:
        model = User
        fields = ['is_staff']



class ProjectFilter(filters.FilterSet):
    members_id = filters.NumberFilter(
        field_name='members__id', lookup_expr='exact')
    username = filters.CharFilter(
        field_name='members__username', lookup_expr='iexact')

    class Meta:
        model = Projects
        fields = []

class TaskFilter(filters.FilterSet):
    user = filters.NumberFilter(
        field_name='user', lookup_expr='exact')
    project = filters.NumberFilter(
        field_name='project', lookup_expr='exact')

    class Meta:
        model =Task
        fields = []

class SuperUserFilter(filters.FilterSet):
    tenant_name= filters.CharFilter(field_name='tenant__name',lookup_expr='exact')
    class Meta:
        model = User
        fields = []

# class TaskFilter(filters.FilterSet):
#     user = filters.NumberFilter(
#         field_name='user', lookup_expr='exact')
#     project = filters.NumberFilter(
#         field_name='project', lookup_expr='exact')

#     class Meta:
#         model =Task
#         fields = []
