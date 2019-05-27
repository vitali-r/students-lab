from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=18)
    avatar = models.ImageField(upload_to='photos/profiles', verbose_name='User\'s photo', blank=True)
    zip_code = models.CharField(max_length=12, blank=True)