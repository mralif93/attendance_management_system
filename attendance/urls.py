from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView, name='attendances'),
  path('history/', views.HistoryView, name='history'),
  path('clock/', views.ClockView, name='clock'),
  path('report/<int:id>/', views.ReportView, name='report'),
]