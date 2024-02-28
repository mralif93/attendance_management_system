from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import CustomUserCreationForm, CustomUserLoginForm, UserForm, ProfileForm, CustomResetPasswordForm
from .models import Profile

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