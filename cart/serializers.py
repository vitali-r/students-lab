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
        validated_data['total_price'] = 0
        order = Order.objects.create(**validated_data)
        if not items:
            raise serializers.ValidationError("Cart is empty")
        else:
            for item in items:
                order.total_price += item.item_price
                item.order = order
                item.save()
            order.save()
            return order
