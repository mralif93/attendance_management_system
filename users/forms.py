from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.forms import ModelForm
from django import forms
from .models import User, Profile

class DateInput(forms.DateInput):
  input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class CustomUserLoginForm(AuthenticationForm):
  class Meta:
    model = User
    fields =  ('username', 'password')

class UserForm(ModelForm):
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'email']

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['user', 'date_of_birth', 'phone', 'address']
    widgets = {
      'date_of_birth': DateInput(),
    }

class CustomResetPasswordForm(PasswordResetForm):
  class Meta:
    model = User
    fields = ('email')