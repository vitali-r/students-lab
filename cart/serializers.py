from rest_framework import serializers
from cart.models import CartItem, Order


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'id',
            'user',
            'product',
            'quantity',
            'item_price',
            'order'
        )


class OrderSerializer(serializers.ModelSerializer):
    cartitems = CartItemSerializer(many=True, read_only=True)

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
        read_only_fields = ('total_price', 'status')

    def create(self, validated_data):
        user = self.context['request'].user
        items = user.items.all()

        if not items:
            raise serializers.ValidationError("Cart is empty")

        total_price = 0
        for item in items:
            total_price += item.item_price

        validated_data['total_price'] = total_price
        order = Order.objects.create(
            **validated_data
        )

        items.update(order_id=order.id)

        return order
