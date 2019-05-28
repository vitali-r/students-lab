from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from products.views import CategoryViewSet, BrandViewSet, ProductViewSet, products


apipatterns = [
    path('', include('products.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', products, name=''),
    path('', include('users.urls'), name='users')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
