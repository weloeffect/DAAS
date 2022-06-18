from urllib import request
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "user_DAAS"
urlpatterns = [
    path("signup", views.register, name="register"),
    path("login", views.signin, name="signin"),
    path("logout", views.signout, name="signout"),
    path("view_profile", views.view_profile, name="view_profile"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("password_reset", views.password_reset, name="password_reset"),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
    #     name='password_change_done'),

    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
    #     name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='html/password_reset-done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'html/password_reset-form.html'), name='password_reset'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='html/password_reset.html'),
     name='password_reset_complete'),
]