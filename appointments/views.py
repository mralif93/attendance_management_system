from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .forms import AppointmentForm
from .models import STATUS_CHOICES, Appointment

# Create your views here.

def AppointmentView(request):
  try:
    # search
    appointments = Appointment.objects.all().order_by('-created_at')
  except Exception as e:
    print(e)
    appointments = None

  context = {
    'appointments': appointments,
  }
  return render(request, 'appointments/index.html', context)


def DetailsAppointmentView(request, id):
  # search
  appointment = Appointment.objects.get(id=id)
  
  context = {
    'appointment': appointment,
  }

  return render(request, 'appointment/details.html', context)


def CreateAppointmentView(request):
  if request.method == 'POST':
    form = AppointmentForm(request.POST or None)
    print(request.POST)

    # valid
    if form.is_valid():
      # save
      form.save()
      # message
      messages.success(request,  "Successfully create the appointment.")
      # redirect
      return redirect('appointments')
    else:
      form = AppointmentForm(request.POST)
  else:
    form = AppointmentForm()
    
  context = {
    'form': form,
  }
  return render(request, 'appointments/create.html', context)


def UpdateAppointmentView(request, id):
  # search
  appointment = Appointment.objects.get(id=id)

  if request.method == 'POST':
    form = AppointmentForm(request.POST, instance=appointment)

    # validate form
    if form.is_valid():
      form.save(commit=False)
      form.updated_at = timezone.now()
      form.save()
      # message
      messages.success(request, "Successfully update the appointment.")
      #  redirect
      return redirect('appointments')
    else:
      form = AppointmentForm(request.POST)
  else:
    form = AppointmentForm(instance=appointment)
    
  context = {
    'form': form,
  }
  return render(request, 'appointments/update.html', context)


def DeleteAppointmentView(request, id):
  # search
  appointment = Appointment.objects.get(id=id)

  if request.method == 'POST':
    form = AppointmentForm(request.POST, instance=appointment)

    # validate form
    if form.is_valid():
      form.save(commit=False)
      form.status = 'Removed' # set status to removed
      form.updated_at = timezone.now()
      form.save()
      # message
      messages.success(request, "Successfully delete the appointment.")
      #  redirect
      return redirect('appointments')
    else:
      form = AppointmentForm(request.POST)
  else:
    form = AppointmentForm(instance=appointment)

  context = {
    'form': form,
  }
  
  # redirect
  return render(request, 'appointments/delete.html', context)
