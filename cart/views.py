from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (ListModelMixin,
                                   DestroyModelMixin,
                                   CreateModelMixin,
                                   RetrieveModelMixin)
from cart.serializers import CartItemSerializer, OrderSerializer
from cart.models import CartItem, Order
from rest_framework.permissions import IsAuthenticated


class CartViewSet(DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        qs = self.queryset.filter(user=self.request.user, order=None)
        return qs


class OrderViewSet(CreateModelMixin,
                   ListModelMixin,
                   RetrieveModelMixin,
                   DestroyModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        qs = self.queryset.filter(user=self.request.user)
        return qs
