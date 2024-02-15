from django.shortcuts import render

# Create your views here.

def AppointmentView(request):
  context = {}
  return render(request, 'appointments/index.html', context)


def CreateAppointmentView(request):
  context = {}
  return render(request, 'appointments/create.html', context)


def UpdateAppointmentView(request):
  context = {}
  return render(request, 'appointments/update.html', context)


def DeleteAppointmentView(request):
  context = {}
  return render(request, 'appointments/delete.html', context)