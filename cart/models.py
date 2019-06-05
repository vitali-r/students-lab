from django.db import models
from django.conf import settings
from products.models import Product


class Order(models.Model):
    STANDART_DELIVERY = 'Standart'
    NEXT_DAY_DELIVERY = 'Next day'
    DEFAULT_ADDRESS = 'Default'
    DIFFERENT_ADDRESS = 'Different'
    IN_PROGRESS = 'In progress'
    COMPLETE = 'Complete'
    PAYPAL = 'Paypal'
    QIWI = 'Qiwi'
    CARD = 'Card'
    CASH = 'Cash'
    ADDRESS_CHOICES = (
        (DEFAULT_ADDRESS, 'Use my default address'),
        (DIFFERENT_ADDRESS, 'Use a different address')
    )
    PAYMENT_CHOICES = (
        (PAYPAL, 'Paypal'),
        (CARD, 'Card'),
        (CASH, 'Cash'),
        (QIWI, 'Qiwi')
    )
    DELIVERY_CHOICES = (
        (STANDART_DELIVERY, 'Standart delivery'),
        (NEXT_DAY_DELIVERY, 'Next day delivery')
    )
    STATUS_CHOICES = (
        (IN_PROGRESS, 'In progress'),
        (COMPLETE, 'Complete')
    )
    ordering_date = models.DateTimeField(auto_now_add=True)
    which_address = models.CharField(
        max_length=255,
        choices=ADDRESS_CHOICES,
        default=DEFAULT_ADDRESS)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    payment_method = models.CharField(
        max_length=25,
        choices=PAYMENT_CHOICES,
        default=CARD)
    delivery_method = models.CharField(
        max_length=25,
        choices=DELIVERY_CHOICES,
        default=STANDART_DELIVERY)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=IN_PROGRESS)
    total_price = models.PositiveIntegerField(editable=False, default=0)


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
