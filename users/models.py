from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        error_messages={'unique': 'This email adress is already used.'}, 
        unique=True, 
        max_length=254, 
        verbose_name='email address')
    address_country = models.CharField(max_length=100, blank=True)
    address_region = models.CharField(max_length=100, blank=True)
    address_city = models.CharField(max_length=100, blank=True)
    address_street = models.CharField(max_length=100, blank=True)
    address_home_number = models.CharField(max_length=10, blank=True)
    address_room_number = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=18)
    avatar = models.ImageField(
        upload_to='photos/profiles',
        verbose_name='User\'s photo',
        blank=True)
    zip_code = models.CharField(max_length=12, blank=True)

    def get_adress(self):
        adress = self.address_home_number + ' ' + self.address_street + '\n' + self.address_city + \
            '\n' + self.address_region + ' ' + self.zip_code + '\n' + self.address_country
        if not(self.address_room_number == ''):
            adress = 'Apt. ' + self.address_room_number + ' ' + adress
        return adress

    def __str__(self):
        return self.username
        