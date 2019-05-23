from rest_framework import viewsets,status,mixins,generics 
from products.models import Category, Brand, Product 
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer 
from .pagination import ProductsResultSetPagination 


class ProductViewSet(mixins.CreateModelMixin, 
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet): 
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    pagination_class = ProductsResultSetPagination 


class CategoryViewSet(mixins.CreateModelMixin, 
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet): 
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer 


class BrandViewSet(mixins.CreateModelMixin, 
                    mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin, 
                    mixins.DestroyModelMixin, 
                    mixins.UpdateModelMixin, 
                    viewsets.GenericViewSet): 
    queryset = Brand.objects.all().prefetch_related('products') 
    serializer_class = BrandSerializer