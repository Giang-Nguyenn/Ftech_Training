from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter

app_name = 'restAPI'

router = SimpleRouter()
router.register('project', views.Project, basename='project-list')
# router.register('project/<int:pk>', views.Project, basename='project-detail')
router.register('task', views.Task, basename='task-list')
# router.register('task/<int:pk>', views.Task, basename='task-detail')
router.register('user', views.Users, basename='user-list')


urlpatterns = [
    # path('demo/', views.home,name='home'),
    path('', include(router.urls)),
    path('test', views.test, name='test'),
    path('project/<int:pk>/users', views.ProjectListUser.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='project-list-user'),
    path('api-token-auth/', views.CustomAuthToken.as_view())
]
