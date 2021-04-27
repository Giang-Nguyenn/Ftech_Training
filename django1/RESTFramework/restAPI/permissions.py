from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Projects
from django.contrib.auth.models import User


class IsUserInProjectPermisson(IsAuthenticated):
    """ 
    Kiểm tra user có thuộc project" hoặc là supperuser 
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user in obj.members.all()
