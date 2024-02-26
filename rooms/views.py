from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.

def ListRoomView(request):
  #  search
  rooms = Room.objects.all().order_by('-created_at')

  context = {
    'rooms': rooms,
  }
  return render(request, 'rooms/index.html', context)


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
  return render(request, 'rooms/create.html', context)


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
  return render(request, 'rooms/details.html', context)


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
  return render(request, 'rooms/update.html', context)


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
  return render(request, 'rooms/delete.html', context)