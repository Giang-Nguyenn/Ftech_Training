from django.urls import path
from . import views
app_name = "app1"
urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('Sign/', views.Sign, name='Sign'),
    path('getSign/', views.getSign, name='getSign'),
    path('postContent/<int:id>', views.postContent, name='postContent'),
    # path('Home/<int:n>', views.Home, name='Home'),
    # path('Home/', views.Home, name='Home'),
    path('Login', views.Login, name='Login'),
    path('A/', views.A, name='A'),
]