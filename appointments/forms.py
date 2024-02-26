from django import forms
from django.forms.widgets import DateInput
from .models import Appointment

#  Create your forms here

class AppointmentForm(forms.ModelForm):
  class Meta:
    model = Appointment
    fields = '__all__'