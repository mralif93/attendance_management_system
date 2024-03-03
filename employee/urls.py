from django.urls import path
from . import views

urlpatterns = [
  path('', views.LoginView, name='login'),
  path('reset-password/', views.ResetPasswordView, name='reset_password'),
  path('register/', views.RegisterView, name='register'),
  path('logout/', views.LogoutView, name='logout'),
  path('profile/<int:id>/', views.ProfileView, name='profile'),
  path('dashboard/', views.DashboardView, name='dashboard'),
  path('qrcode/<int:id>/', views.QRCodeView, name='qrcode'),
]