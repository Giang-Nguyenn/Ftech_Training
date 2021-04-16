from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter

app_name='serializers'

router=DefaultRouter()
router.register('student', views.StudentList1, basename='student-list')
router.register('student/<int:pk>', views.StudentList1, basename='student-detail')
urlpatterns = [
    path('demo/', views.home,name='home'),
    path('', include(router.urls)),
    # path('student/<int:id>', views.StudentDetail.as_view(),name='student-detail'),

    # path('student/', views.StudentList.as_view(),name='student_list'),
    # path('student1/', views.StudentCRUD1.as_view(),name='student_list1'),

    # path('student1/', views.StudentList1.as_view({'get': 'list','post':'create'}),name='student_list'),
    # path('student1/<int:pk>', views.StudentList1.as_view({'get': 'retrieve','put':'update','delete':'destroy'}),name='student_list'),
    # path('student/<int:pk>/partial', views.StudentList1.as_view({'put':'update','patch': 'partial_update'}),name='partial_update'),

    # path('student/<int:id>', views.StudentDetail.as_view(),name='student_detail'),
    # path('student_list/', views.StudentList.as_view(),name='student_listt'),
    # # path('', include('Serializers.urls')),


]