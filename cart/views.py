from rest_framework import viewsets
from cart.serializers import CartItemSerializer, OrderSerializer
from cart.models import CartItem, Order
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CartViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = CartItem.objects.filter(user_id=user_id)
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        queryset = Order.objects.filter(user_id=user_id)
        return queryset