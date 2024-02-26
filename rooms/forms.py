from django import forms
from .models import Room

#  Create your forms here

class  RoomForm(forms.ModelForm):
  class Meta:
    model = Room
    fields = '__all__'
