from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter, SimpleRouter


router = SimpleRouter()
router.register('project', views.ProjectsView, basename='project-list')
urlpatterns = [
    path('', include(router.urls)),
    path('test', views.test,name='test'),
]