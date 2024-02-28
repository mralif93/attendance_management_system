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

STATUS_CHOICES = [
  ('BOOKED', 'Booked'),
  ('CANCELLED', 'Canceled'),
  ('COMPLETED', 'Completed'),
  ('IN PROGRESS', 'In Progress'),
  ('REMOVED', 'Removed'),
]

class Appointment(models.Model):
  title = models.CharField(max_length=200, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="appointments")
  start = models.DateTimeField()
  end = models.DateTimeField()
  status = models.CharField(choices=STATUS_CHOICES, default=None, max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.room.name