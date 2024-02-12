from django.urls import path
from . import views

urlpatterns = [
  path('', views.LandingView, name='landing'),
  path('history/', views.HistoryView, name='history'),
  path('clock-in/', views.ClockInView, name='clock_in'),
  path('clock-out/', views.ClockOutView, name='clock_out'),
]