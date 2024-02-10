from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.LandingView, name='landing_page'),
]