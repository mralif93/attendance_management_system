from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Attendance, User

# Create your views here.
def LandingView(request):
  records = Attendance.objects.all().order_by('-created_at')
  context = {
    'records': records,
  }
  return render(request, 'attendance/landing.html', context)

@login_required()
def HistoryView(request):
  records = Attendance.objects.all().order_by('-created_at')
  context = {
    'records': records,
  }
  return render(request, 'attendance/history.html', context)

def ClockInView(request):
  if request.method == "POST":
    username = request.POST['username']

    try:
      user = User.objects.get(username=username)

      # get current datetime
      today = timezone.now()
      attendance = Attendance.objects.filter(user=user, created_at__year=today.year, created_at__month=today.month, created_at__day=today.day)
      
      # already checked in today
      if len(attendance) == 0:
        record = Attendance(user=user, clock_in=today, created_at=today)
        record.save()
      else:
        messages.warning(request, 'Attendance is already check in!')
        
    except Exception as e:
      messages.error(request, e)

  return redirect('landing')

def ClockOutView(request):
  if request.method == "POST":
    username = request.POST['username']

    try:
      user = User.objects.get(username=username)

      # get current datetime
      today = timezone.now()
      attendance = Attendance.objects.filter(user=user, created_at__year=today.year, created_at__month=today.month, created_at__day=today.day)
      
      # already checked in today
      if attendance is not None:
        record = Attendance.objects.get(user=user, created_at__year=today.year, created_at__month=today.month, created_at__day=today.day)
        record.clock_out = timezone.now()
        record.save()
      else:
        pass
    except Exception as e:
      messages.error(request, e)
  
  return redirect('landing')