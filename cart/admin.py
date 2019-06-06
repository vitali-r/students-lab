from django.contrib import admin
from .models import CartItem, Order, Promocode


admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(Promocode)
