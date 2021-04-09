from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
app_name='serializers'

urlpatterns = [
    path('demo/', views.home,name='home'),
    path('student/', views.StudentList.as_view(),name='student_list'),
    path('student/<int:id>', views.StudentDetail.as_view(),name='student_detail'),
    # path('', include('Serializers.urls')),
]