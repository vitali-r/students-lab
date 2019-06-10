from django.urls import path, include
from cart import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.CartViewSet)
router.register(r'orders', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
