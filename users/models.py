from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        error_messages={'unique': 'This email address is already used.'},
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
    is_active = models.BooleanField(
        default=False,
        help_text='Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts.',
        verbose_name='active')

    def get_adress(self):
        address = '{0} {1}\n{2}\n{3} {4}\n{5}'.format(
            self.address_home,
            self.address_street,
            self.address_city,
            self.address_region,
            self.zip_code,
            self.address_country)
        if not(self.address_room_number == ''):
            address = 'Apt. ' + self.address_room_number + ' ' + address
        return address

    def __str__(self):
        return self.username
