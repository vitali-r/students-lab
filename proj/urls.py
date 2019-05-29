from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import products


apipatterns = [
    path('', include('products.urls')),
    path('products/<int:product_id>/comments', include('comments.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', products, name='')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
