from django.urls import path
from . import views

urlpatterns = [
  path('', views.AppointmentView, name='appointments'),
  path('create/', views.CreateAppointmentView, name='create_appointment'),
  path('update/<int:id>/', views.UpdateAppointmentView, name='update_appointment'),
  path('delete/<int:id>/', views.DeleteAppointmentView, name='delete_appointment'),
]