from rest_framework import routers 
from products.views import CategoryViewSet, BrandViewSet, ProductViewSet 


router = routers.DefaultRouter() 
router.register(r'products', ProductViewSet) 
router.register(r'brands', BrandViewSet) 
router.register(r'categories', CategoryViewSet) 


urlpatterns = router.urls