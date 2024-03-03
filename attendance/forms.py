from django import forms
from .models import Attendance

# Create your forms here.
REMARK_CHOICES = {
  ('1', 'DR Activities'),
  ('2', 'Deployment'),
  ('3', 'Support Issue/s'),
  ('4', 'Time Off 2 Hours'),
  ('5', 'Family Matters'),
  ('6', 'Half Day - AM'),
  ('7', 'Half Day - PM'),
  ('8', 'Late - Raining'),
}

class CheckInCheckOutForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['clock_in', 'clock_out']