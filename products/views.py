from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .serializers import (ProductSerializer,
                          ProductAttributeSerializer,
                          CategorySerializer,
                          BrandSerializer,
                          AttributeSerializer)
from .models import Product, Brand, Category, Attribute, ProductAttribute
from .permissions import IsAdminUserOrReadOnly
from django.views.generic import TemplateView


def products(request):
    return render(request, 'products.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().prefetch_related('product_attributes')
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().prefetch_related('products')
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly, )

class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly, )

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().prefetch_related('products')
    serializer_class = BrandSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
