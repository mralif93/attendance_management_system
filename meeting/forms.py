from django import forms
from django.forms.widgets import DateInput
from .models import Room, Appointment

#  Create your forms here
class  RoomForm(forms.ModelForm):
  class Meta:
    model = Room
    fields = '__all__'
    
class AppointmentForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = '__all__'