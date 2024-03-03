from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from cryptography.fernet import Fernet
from .forms import CustomUserCreationForm, CustomUserLoginForm, UserForm, ProfileForm, CustomResetPasswordForm
from .models import Profile

import os
import qrcode
from PIL import Image
from io import BytesIO
import base64

# Create your views here.

@login_required()
def RegisterView(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    
    if form.is_valid():
      user = form.save()

      # Clean form
      uname = form.cleaned_data['username']
      fname = form.cleaned_data['first_name']
      lname = form.cleaned_data['last_name']
      email = form.cleaned_data['email']
      
      profile = Profile(employee=User.objects.get(username=uname))
      profile.save()

      # Log the new user in
      # user = authenticate(request=request, username=uname, password=password.value())
      # login(request, user)

      # redirect
      return redirect('dashboard')
  else:
    form = CustomUserCreationForm()

  context = {
    'form': form,
  }
  return render(request, 'employee/register.html', context);


def LoginView(request):
  if request.user.is_authenticated:
    return redirect('dashboard')
    
  if request.method == 'POST':
    form = CustomUserLoginForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('dashboard')
  else:
    form = CustomUserLoginForm()
  
  context = {
    'form': form,
  }
  return render(request, 'employee/login.html', context)


@login_required()
def LogoutView(request):
  logout(request)
  return redirect('login')


@login_required()
def DashboardView(request):
  try:
    users = User.objects.filter(is_superuser=False).order_by('-date_joined')
  except ObjectDoesNotExist:
    messages.error(request, "Error: No user!")

  context = {
    'users': users,
  }
  return render(request, 'employee/dashboard.html', context)


@login_required()
def ProfileView(request, id):
  # search data
  user = User.objects.get(id=id)
  profile = Profile.objects.get(employee=user)

  form1 = UserForm(instance=user)
  form2 = ProfileForm(instance=profile)

  # post
  if request.method == 'POST':
    form1 = UserForm(request.POST, instance=user)
    form2 = ProfileForm(request.POST, instance=profile)

    if form1.is_valid() and form2.is_valid():
      form1.save()
      form2.save()

      # redirect to dashboard
      return redirect('dashboard')

  context = {
    'form1': form1,
    'form2': form2,
  }
  return render(request, 'employee/profile.html', context)


def ResetPasswordView(request):
  if request.method == 'POST':
    # form
    form = CustomResetPasswordForm(request.POST)
    # valid form
    if form.is_valid():
      # get data
      email = form.cleaned_data['email']
      # search email
      user = User.objects.get(email=email)
      # user exist
      if user.exists():
        pass
    
    #   form.save()
  else:
    form = CustomResetPasswordForm()

  context = {
    'form': form,
  }
  return render(request, 'employee/password-reset.html', context)


def QRCodeView(request, id):
  try:
    # get employee details
    employee = User.objects.get(id=id)
    # we need to define the encryption key
    # fernet can handle this with using generate_key() method
    encryption_key = Fernet.generate_key()
    # now create out Fernet object
    cipher_suite = Fernet(encryption_key)
    # convert string to bytes
    string = str(employee.username).encode('utf-8')
    # now we can convert plaintext to ciphertext
    encrypted_value = cipher_suite.encrypt(string)
    print(encrypted_value)
    deccrypted_value = cipher_suite.decrypt(encrypted_value)
    print(deccrypted_value)
    print(deccrypted_value.decode('utf-8'))
    
    # generate qrcode
    qr_image = qrcode.make(encrypted_value, box_size=15)
    qr_image_pil = qr_image.get_image()
    stream = BytesIO()
    qr_image_pil.save(stream, format='PNG')
    qr_image_data = stream.getvalue()
    qr_image_base64 = base64.b64encode(qr_image_data).decode('utf-8')

    context = {
      'employee': employee,
      'qr_image_base64': qr_image_base64,
    }
    return render(request, "employee/qrcode.html", context)
  except User.DoesNotExist:
    messages.warning(request, "Employee does not exist.")
    return redirect('dashboard')


@csrf_exempt
def ScanQRCode(request):
  """Handle POST requests from the /qrcode/?action=scan view."""
  data = json.loads(request.body.decode())
  username = data["username"]
  timestamp = datetime.fromisoformat(data["timestamp"])

  try:
    employee = Employee.objects.get(user__username=username)
    Attendance.log_entry(employee, timestamp)
    response_data = {"message": "Successfully logged attendance"}
    status = 200
  except KeyError as e:
    response_data = {f"Missing field: {e}"}, 400
  except Employee.DoesNotExist:
    response_data = {"error": "User not found"}, 404

  return JsonResponse(response_data, status=status)
