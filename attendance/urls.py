from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView, name='attendances'),
  path('history/', views.HistoryView, name='history'),
  path('clocking/', views.ClockingView, name='clocking'),
  path('report/<int:id>/', views.ReportView, name='report'),
  path('qr-scanner/', views.ScannerView, name='scanner'),
]