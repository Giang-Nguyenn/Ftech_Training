from django.urls import path
from . import views
app_name = "app1"
urlpatterns = [
    path('home/', views.home, name='home'),
    path('home_user/', views.home_user, name='home_user'),
    path('add_post/', views.add_post, name='add_post'),
    path('sign/', views.sign, name='sign'),
    path('get_sign/', views.get_sign, name='get_sign'),
    path('post_content/<int:id>', views.post_content, name='post_content'),
    # path('Home/<int:n>', views.Home, name='Home'),
    # path('Home/', views.Home, name='Home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('A/', views.A, name='A'),
]