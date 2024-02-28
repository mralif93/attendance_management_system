from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Room, Appointment, STATUS_CHOICES
from .forms import RoomForm, AppointmentForm

# Create your views here.
def MeetingView(request):
  context = {}
  return render(request, 'meeting/index.html', context)


def ListRoomView(request):
  #  search
  rooms = Room.objects.all().order_by('-created_at')

  context = {
    'rooms': rooms,
  }
  return render(request, 'meeting/room/index.html', context)


def CreateRoomView(request):
  # submit
  if request.method == 'POST':
    form = RoomForm(request.POST or None)
    # validate form
    if form.is_valid():
      # save form
      form.save()
      # message
      # redirect
      return redirect('rooms')
  else:
    form = RoomForm()

  context = {
    'form': form,
  }
  return render(request, 'meeting/room/create.html', context)


def DetailsRoomView(request, id):
  # search
  room = Room.objects.get(id=id)

  # submit
  if request.method == 'POST':
    form = RoomForm(instance=room)

    # validate form
    if form.is_valid():
      # save form
      form.save()
  else:
    form = RoomForm(instance=room)

  context = {
    'form': form,
  }
  return render(request, 'meeting/room/details.html', context)


def UpdateRoomView(request, id):
  # search
  room = Room.objects.get(id=id)

  # submit
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)

    # validate form
    if form.is_valid():
      # save form
      form.save()
      # message
      # redirect
      return redirect('rooms')
  else:
    form = RoomForm(instance=room)

  context = {
    'form': form,
  }
  return render(request, 'meeting/room/update.html', context)


def DeleteRoomView(request, id):
  # search
  room = Room.objects.get(id=id)

  # submit
  if request.method == 'POST':
    # change status to deleted
    room.is_active = False
    room.save()
    # message
    # redirect
    return redirect('rooms')

  context = {
    'room': room,
  }
  return render(request, 'meeting/room/delete.html', context)


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
  return render(request, 'meeting/appointment/index.html', context)


def DetailsAppointmentView(request, id):
  # search
  appointment = Appointment.objects.get(id=id)
  
  context = {
    'appointment': appointment,
  }

  return render(request, 'meeting/appointment/details.html', context)


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
  return render(request, 'meeting/appointment/create.html', context)


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
  return render(request, 'meeting/appointment/update.html', context)


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
  return render(request, 'meeting/appointment/delete.html', context)