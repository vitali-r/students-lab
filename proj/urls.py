from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import (products, index,
                            products_detail)
from rest_framework_jwt.views import refresh_jwt_token
from users.views import ObtainCustomJSONWebToken


apipatterns = [
    path('', include('products.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api')),
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('products/<int:product_id>/', products_detail, name='products_detail'),
    path('', include('users.urls'), name='users'),
    path('sign-in/', ObtainCustomJSONWebToken.as_view()),
    path('api/sign-in/refresh', refresh_jwt_token)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
