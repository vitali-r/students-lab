from cart.views import CartViewSet, OrderViewSet
from django.conf.urls import url


urlpatterns = [
    url(r'', CartViewSet.as_view({'get': 'list'}), name='cart-list'),
    url(r'orders', OrderViewSet.as_view({'get': 'list'}), name='order-list')
]