from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name= 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('change-password', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html', success_url="queue_management:update-queue"), name='change-password'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
