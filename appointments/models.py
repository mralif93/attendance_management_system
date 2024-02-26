from django.db import models
from rooms.models import Room

# Create your models here.

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
  room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="reservations")
  start = models.DateTimeField()
  end = models.DateTimeField()
  status = models.CharField(choices=STATUS_CHOICES, default=None, max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.room.name