from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from .models import Attendance, User

# Create your views here.
def IndexView(request):
  # get current datetime
  today = datetime.now()
  # search records
  records = Attendance.objects.filter(clock_in__date=today.date()).order_by('-created_at')
  context = {
    'records': records,
  }
  return render(request, 'attendance/index.html', context)

@login_required()
def HistoryView(request):
  records = Attendance.objects.all().order_by('-created_at')
  context = {
    'records': records,
  }
  return render(request, 'attendance/history.html', context)

@login_required()
def ReportView(request, id):
  try:
    # search user
    user = User.objects.get(username=id)

    # get current datetime
    today = datetime.now()

    # search attendance list
    attendances = Attendance.objects.filter(user=user)

    # send message

  except Exception as e:
    print(e)
    # empty
    attendances = None

  context = {
    'attendances': attendances,
  }
  return render(request, 'attendance/report.html', context)


def ClockingView(request):
  if request.method == "POST":
    username = request.POST['username']

    try:
      # get user
      user = User.objects.get(username=username)
      # get current datetime
      today = datetime.now()

      # search for existing record of the same day and user
      existing = Attendance.objects.filter(employee=user).filter(clock_in__date=today.date()).first()

      if existing is None:
        # create a new attendance record
        new_record = Attendance(employee=user, clock_in=today, created_at=today)
        new_record.save()
        messages.success(request, f"Successfully clocked in as {username}.")
      else:
        # update the existing record with the time out
        existing.clock_out = today
        existing.save()
        messages.info(request, f"Updated previous check-in from {existing.clock_in} to {existing.clock_out}.")
        messages.info(request, f"{username} has been updated.")
    
    except Exception as e:
      messages.error(request, e)

  return redirect('attendances')


def ScannerView(request):
  context = {}
  return render(request, 'attendance/scanner.html', context)