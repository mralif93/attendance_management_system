from django.contrib import admin
from .models import Attendance
import datetime

# Register your models here.
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
  search_fields = ['employee', 'clock_in', 'clock_out', 'created_at', 'updated_at']
  list_display = ['fullname', 'clock_in', 'clock_out', 'created_at']

  def fullname(self, obj):
    return obj.employee.first_name + " " + obj.employee.last_name
  
