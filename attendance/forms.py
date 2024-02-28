from django import forms
from .models import Attendance

# Create your forms here.
class CheckInCheckOutForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['clock_in', 'clock_out']