from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'restAPI'

router = DefaultRouter()
router.register('project', views.Project, basename='project-list')
router.register('project/<int:pk>', views.Project, basename='project-detail')
# router.register('projectuser/', views.ProjectListUser,basename='projectuser-list'),
# router.register('project_user/<int:pk>', views.ProjectListUser, basename='project_user-list')
router.register('task', views.Task, basename='task-list')
router.register('task/<int:pk>', views.Task, basename='task-detail')


urlpatterns = [
    # path('demo/', views.home,name='home'),
    path('', include(router.urls)),
    path('test', views.test, name='test'),
    # path('logout', views.logout, name='logout'),
    path('project/user', views.ProjectListUser.as_view(
        {'get': 'list', 'post': 'create'}), name='project-list-user'),
    path('api-token-auth/', views.CustomAuthToken.as_view())

]
