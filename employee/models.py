from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  employee = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  date_of_birth = models.DateField(blank=True, null=True)
  phone = models.CharField(max_length=15, blank=True, null=True)
  address = models.TextField(blank=True, null=True)
  
  def __str__(self):
    return self.employee.first_name + " " + self.employee.last_name