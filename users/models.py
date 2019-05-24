from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    adress = models.CharField(max_length = 256, blank = True)
    phone = models.CharField(max_length = 18, default = '+')
    avatar = models.ImageField(upload_to = 'photos/profiles', verbose_name = 'User\'s photo')
    user = models.OneToOneField(User, on_delete = models.CASCADE)