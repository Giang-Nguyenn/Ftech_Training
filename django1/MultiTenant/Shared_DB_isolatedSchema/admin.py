# from django.contrib import admin
# from .models import Tenant1,Projects1,UserProject1,Task1

# from .utils import tenant_from_request
# # Register your models here.
# class CustomAdmin(admin.ModelAdmin):
#     def get_queryset(self, request, *args, **kwargs):
#         queryset = super().get_queryset(request, *args, **kwargs)
#         tenant = tenant_from_request(request)
#         queryset = queryset.filter(tenant=tenant)
#         return queryset

#     def save_model(self, request, obj, form, change):
#         tenant = tenant_from_request(request)
#         obj.tenant = tenant
#         super().save_model(request, obj, form, change)

# admin.site.register(Tenant1)

# @admin.register(Projects1)
# class ProjectsAdmin(CustomAdmin):
#     fields = ['name','describe','status','note']
#     # fields =[field.name for field in Projects._meta.fields if field.name not in ['id','members']]


# @admin.register(UserProject1)
# class UserProjectAdmin(CustomAdmin):
#     fields = ['project','user']

# @admin.register(Task1)
# class TaskAdmin(CustomAdmin):
#     fields = ['name','project','user','describe','status','start','end','dead_line','note']