from django.urls import path
from . import views

urlpatterns = [
  path('', views.ListRoomView, name='rooms'),
  path('create/', views.CreateRoomView, name='create_room'),
  path('view/<int:id>/', views.DetailsRoomView, name='details_room'),
  path('update/<int:id>/', views.UpdateRoomView, name='update_room'),
  path('delete/<int:id>/', views.DeleteRoomView, name='delete_room'),
]