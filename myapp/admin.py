from django.contrib import admin
from .models import User,Patient,Doctor

admin.site.register((User,Patient,Doctor))

