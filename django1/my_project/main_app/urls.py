from django.urls import path
from . import views
app_name = "main_app"

urlpatterns = [
    # path('', views.home, name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('projects/<int:id>/', views.ViewProject.as_view(), name='project'),
    path('task/<int:id>/', views.ViewTask.as_view(), name='task'),
    path('add_project/', views.AddProject.as_view(), name='add_project'),
    path('add_task/', views.AddTask.as_view(), name='add_task'),
    path('demo/', views.demo, name='demo'),
]