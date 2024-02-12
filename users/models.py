from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
      """Create and save a User with the given email and password."""
      if not email:
        raise ValueError('The given email must be set')
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user

    def create_user(self, email, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', False)
      extra_fields.setdefault('is_superuser', False)
      return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
      """Create and save a SuperUser with the given email and password."""
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)

      if extra_fields.get('is_staff') is not True:
        raise ValueError('Superuser must have is_staff=True.')
      if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

      return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
  pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
      return self.user.first_name + " " + self.user.last_name