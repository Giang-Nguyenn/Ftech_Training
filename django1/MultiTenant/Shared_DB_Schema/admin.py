from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tenant, Projects, UserProject, Task, User
# from django.contrib.auth.models import User
from .utils import tenant_from_request
# Register your models here.


# admin.site.unregister(User)
# @admin.register(UserCustom)
# class CustomUserAdmin(UserAdmin):
#     pass
class CustomAdmin(admin.ModelAdmin):
    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)


@admin.register(User)
class UsersAdmin(CustomAdmin):
    fields = [field.name for field in User._meta.fields if field.name not in ['id']]


@admin.register(Projects)
class ProjectsAdmin(CustomAdmin):
    fields = ['name', 'describe', 'status', 'note']
    # fields =[field.name for field in Projects._meta.fields if field.name not in ['id','members']]


@admin.register(UserProject)
class UserProjectAdmin(CustomAdmin):
    fields = ['project', 'user']


@admin.register(Task)
class TaskAdmin(CustomAdmin):
    fields = ['name', 'project', 'user', 'describe',
              'status', 'start', 'end', 'dead_line', 'note']
