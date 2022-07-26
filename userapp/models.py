from django.db import models

from django.contrib.auth.models import AbstractUser
from datetime import time

class UserProfile(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='users/%Y/%m/%d/')
    bio = models.CharField(max_length=300, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    @property
    def age(self):
      return date.today().year - self.birthday.year

