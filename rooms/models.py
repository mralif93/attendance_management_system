from django.db import models

# Create your models here.

class Room(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  descriptions = models.TextField(max_length=200, blank=True, null=True)
  is_active = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name