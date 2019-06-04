from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from products.views import products, index
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


apipatterns = [
    path('', include('products.urls')),
    path('products/<int:product_id>/comments', include('comments.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((apipatterns, 'api'), namespace='api')),
    path('', index, name='index'),
    path('products/', products, name='products')
    path('', include('users.urls'), name='users'),
    path('api/auth/', obtain_jwt_token),
    path('api/auth/refresh', refresh_jwt_token)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
