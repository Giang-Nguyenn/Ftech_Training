from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter


router = SimpleRouter()
router.register('project', views.Project, basename='project-list')
router.register('task', views.Task, basename='task-list')
router.register('user', views.Users, basename='user-list')
router.register('tenant', views.TenantView, basename='tenant-list')
router.register('tenant_all', views.TenantAll, basename='tenant-list')
router.register('superuser', views.CreateSuperUser, basename='superuser')


urlpatterns = [
    path('', include(router.urls)),
    path('test', views.test, name='test'),
    path('project/<int:pk>/users', views.ProjectListUser.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='project-list-user'),
    path('api-token-auth/', views.CustomAuthToken.as_view())
]