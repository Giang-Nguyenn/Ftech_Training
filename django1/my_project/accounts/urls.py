from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = "accounts"
urlpatterns = [

    path('home/', views.home, name='home'),
    # path('sent/', views.sent, name='sent'),

    path('edit/', views.Edit.as_view(), name='edit'),

    path('sign/', views.Sign.as_view(), name='sign'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logged_out.html'), name='logout'),

    path('logout_then_login/', auth_views.logout_then_login,
         name='logout_then_login'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html',
                                                                   success_url=reverse_lazy('accounts:password_change_done')),
         name='password_change'),  # *

    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/home.html'), name='password_change_done'),

    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                                                email_template_name='registration/password_reset_email.html',
                                                                subject_template_name='registration/password_reset_subject.txt',
                                                                success_url=reverse_lazy('accounts:password_reset_done')),
         name='password_reset'),


    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',
                                                                                success_url=reverse_lazy('accounts:password_reset_complete')),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
