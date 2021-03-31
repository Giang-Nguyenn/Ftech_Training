from django.urls import path
from . import views
app_name = "main_app"

urlpatterns = [
    # path('', views.home, name='home'),
    path('home/', views.Home.as_view(), name='home'),
    path('projects/<int:id>/', views.ViewProject.as_view(), name='project'),
    path('view_task/<int:id>/', views.ViewTask.as_view(), name='view_task'), #
    path('update_task/<int:id>/', views.TaskCRUD.as_view(), name='update_task'), # Update task,id là id task
    # path('add_project/', views.AddProject.as_view(), name='add_project'),
    path('projects/add_project/', views.ProjectCRUD.as_view(), name='add_project'),# thêm sửa xoá cập nhậT
    path('projects/update_project/', views.ProjectCRUD.as_view(), name='update_project'),# thêm sửa xoá cập nhậT
    path('projects/<int:id>/project_add_user/', views.UpdateUserProject.as_view(), name='project_add_user'),# thêm sửa xoá cập nhậT
    path('projects/<int:id>/project_del_user/', views.UpdateUserProject.as_view(), name='project_del_user'),# thêm sửa xoá cập nhậT
    # path('add_del_task/', views.Add_Del_Task.as_view(), name='add_del_task'),
    path('add_task/<int:id>', views.TaskCRUD.as_view(), name='add_task'),# thêm task ,id là id project cần thêm task
    path('demo/', views.demo, name='demo'),
]