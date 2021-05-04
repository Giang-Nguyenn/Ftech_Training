from django_filters import rest_framework as filters
from django.contrib.auth.models import User


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = User
        fields = ['is_staff']


# class ProjectFilter(filters.FilterSet):
#     class Meta:
#         model = User
#         fields = ['id', 'is_staff']
