from django import forms
from .models import Attendance

# Create your forms here.

class CheckInCheckOutForm(forms.ModelForm):
  class Meta:
    model = Attendance
    fields = ['clock_in', 'clock_out']
    labels = {
      "clock_in": "",
      "clock_out": ""
    }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(CheckInCheckOutForm, self).__init__(*args, **kwargs)
        
        if not self.instance.pk: # If it's a new entry
          self.fields['clock_in'].initial = self.user
          
          # Hide the clock out field until there is an actual time to compare against
          self.fields["clock_out"].widget.attrs["style"] = "display: none"
          self.fields["clock_out"].required = False