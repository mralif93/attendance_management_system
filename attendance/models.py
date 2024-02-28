from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Attendance(models.Model):
  employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
  clock_in = models.DateTimeField(blank=True, null=True)
  clock_out = models.DateTimeField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.employee.first_name + " " + self.employee.last_name