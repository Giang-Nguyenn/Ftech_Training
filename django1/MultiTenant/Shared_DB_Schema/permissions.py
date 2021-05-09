from rest_framework.permissions import BasePermission, IsAuthenticated
from .models import Projects,User
# from django.contrib.auth.models import User


class IsUserInProjectPermisson(IsAuthenticated):
    """ 
    Kiểm tra user có thuộc project" hoặc là supperuser 
    """
    message = "Người dùng không nằm trong project này"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user in obj.members.all()


class UserInProjectPermisson(BasePermission):
    """ 
    Kiểm tra user có thuộc project" hoặc là supperuser 
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user in obj.members.all()


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.supper_admin)
