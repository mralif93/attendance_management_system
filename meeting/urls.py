from django.urls import path
from . import views

urlpatterns = [
  path('', views.MeetingView, name='meeting'),
  path('rooms/', views.ListRoomView, name='rooms'),
  path('rooms/create/', views.CreateRoomView, name='create_room'),
  path('rooms/details/<int:id>/', views.DetailsRoomView, name='details_room'),
  path('rooms/update/<int:id>/', views.UpdateRoomView, name='update_room'),
  path('rooms/delete/<int:id>/', views.DeleteRoomView, name='delete_room'),
  path('appointments/', views.AppointmentView, name='appointments'),
  path('appointments/create/', views.CreateAppointmentView, name='create_appointment'),
  path('appointments/details/<int:id>/', views.DetailsAppointmentView, name='details_appointment'),
  path('appointments/update/<int:id>/', views.UpdateAppointmentView, name='update_appointment'),
  path('appointments/delete/<int:id>/', views.DeleteAppointmentView, name='delete_appointment'),
]