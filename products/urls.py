from django.urls import path, include
from rest_framework import routers
from products.views import (CategoryViewSet,
                            BrandViewSet,
                            ProductViewSet,
                            AttributeViewSet,
                            ProductAttributeViewSet,
                            CategoryListViewSet)


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'attributes', AttributeViewSet)
router.register(r'categoriess', CategoryListViewSet)



urlpatterns = router.urls
