from django.db import models
from django.conf import settings
from products.models import Product


class Promocode(models.Model):
    promo_code = models.CharField(max_length=25)
    discount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return 'Promo code for a {}% discount'.format(self.discount)


class Order(models.Model):
    STANDART_DELIVERY = 'Standart'
    NEXT_DAY_DELIVERY = 'Next day'
    SUBMITTED = 'Submitted'
    APPROVED = 'Approved'
    IN_PROGRESS = 'In progress'
    COMPLETE = 'Complete'
    PAYPAL = 'Paypal'
    QIWI = 'Qiwi'
    CARD = 'Card'
    CASH = 'Cash'
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
        (SUBMITTED, 'Submitted'),
        (APPROVED, 'Approved'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETE, 'Complete')
    )
    created_at = models.DateTimeField(auto_now_add=True)
    use_default_address = models.BooleanField(default=False)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=25)
    payment_method = models.CharField(
        max_length=25,
        choices=PAYMENT_CHOICES,
        default=CARD)
    delivery_method = models.CharField(
        max_length=25,
        choices=DELIVERY_CHOICES,
        default=STANDART_DELIVERY)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=SUBMITTED)
    promo_code = models.CharField(max_length=25)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return 'Order {}, creation time: {}, status: {}, customer phone: {}'.format(
            self.id,
            self.created_at,
            self.status,
            self.phone)


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    @property
    def item_price(self):
        return round(self.product.price * self.quantity, 2)

    def save(self, *args, **kwargs):
        order = Order.objects.get(pk=self.order.id)
        promocode = Promocode.objects.get(promo_code=order.promo_code)
        order.total_price += self.item_price
        if promocode.promo_code == order.promo_code:
            order.total_price = round(order.total_price * (100 - promocode.discount) / 100, 2)
        order.save()
        super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return 'Item with {} {}, price - {}'.format(
            self.quantity,
            self.product.name,
            self.item_price)
