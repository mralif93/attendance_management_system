from django.db import models
from users.models import User

# Create your models here.

class Attendance(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  clock_in = models.DateTimeField(blank=True, null=True)
  clock_out = models.DateTimeField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.first_name + " " + self.user.last_name