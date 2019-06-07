from rest_framework import serializers
from cart.models import CartItem, Order
from django.conf import settings


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'id',
            'user',
            'product',
            'quantity',
            'item_price'
        )


class OrderSerializer(serializers.ModelSerializer):
    cartitems = CartSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'created_at',
            'use_default_address',
            'payment_method',
            'phone',
            'delivery_method',
            'status',
            'total_price',
            'address',
            'cartitems'
        )
