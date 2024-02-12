from django import forms
from .models import Attendance

# Create your forms here.

class CheckInForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['clock_in']

class CheckOutForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['clock_out']