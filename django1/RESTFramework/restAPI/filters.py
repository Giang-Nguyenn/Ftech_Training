from django_filters import rest_framework as filters
from django.contrib.auth.models import User

from .models import Projects


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='exact')
    username__iexact = filters.CharFilter(
        field_name='username', lookup_expr='iexact')

    class Meta:
        model = User
        fields = ['is_staff']

# class UserFilter(filters.FilterSet):
#     class Meta:
#         model = User
#         fields = {'is_staff': ['iexact'],
#                   'username': ['exact', 'iexact'],
#                   'id': ['gt', 'lt'],
#                   }


class ProjectFilter(filters.FilterSet):
    members_id = filters.NumberFilter(
        field_name='members__id', lookup_expr='exact')
    username = filters.CharFilter(
        field_name='members__username', lookup_expr='iexact')

    class Meta:
        model = Projects
        fields = []
