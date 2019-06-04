from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (ProductSerializer,
                          ProductAttributeSerializer,
                          CategorySerializer,
                          BrandSerializer,
                          AttributeSerializer)
from .models import Product, Brand, Category, Attribute, ProductAttribute
from .permissions import IsAdminUserOrReadOnly


def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('product_attributes')
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
    filterset_fields = ('brand',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('products')
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly, )
    filterset_fields = ('name',)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().prefetch_related('products')
    serializer_class = BrandSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
    filterset_fields = ('name',)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
