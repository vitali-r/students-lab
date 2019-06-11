from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import (products, index,
                            products_detail)


apipatterns = [
    path('', include('products.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:product_id>/', products_detail, name='products_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
