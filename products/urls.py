from rest_framework import routers
from products.views import (CategoryViewSet,
                            BrandViewSet,
                            ProductViewSet,
                            AttributeViewSet)


router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'attributes', AttributeViewSet, basename='attributes')


urlpatterns = router.urls
