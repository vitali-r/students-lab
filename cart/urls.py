from django.urls import path, include
from cart import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet)
router.register(r'', views.CartViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
