# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create a custom user model with profile picture and address fields
class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    address_line1 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    pincode = models.CharField(max_length=10, blank=True)

# Create a patient model with a one-to-one relation to the user model
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

# Create a doctor model with a one-to-one relation to the user model
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

