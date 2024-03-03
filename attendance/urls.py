from django.urls import path
from . import views

urlpatterns = [
  path('', views.IndexView, name='attendances'),
  path('history/', views.HistoryView, name='history'),
  path('clocking/', views.ClockingView, name='clocking'),
  path('report/<int:id>/', views.ReportView, name='report'),
  # path('qrcode/', views.QRCodeView, name='qrcode'),
  path('qr-scan/', views.QRScanView, name='qrscan'),
  path('qr-scanner/<str:id>/', views.QRScannerView, name='qrscanner'),
]