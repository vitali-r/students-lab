from rest_framework import serializers 
from products.models import Category, Brand, Product 


class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product 
        fields = ( 
        'id', 
        'name', 
        'description', 
        'price', 
        'ram', 
        'color', 
        'discount', 
        'image', 
        'brand', 
        'category' 
        ) 


class BrandSerializer(serializers.ModelSerializer): 
    products = ProductSerializer(many=True) 
    class Meta: 
        model = Brand 
        fields = ( 
        'id', 
        'name', 
        'description', 
        'image', 
        'products' 
        ) 


class CategorySerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Category 
        fields = ('id', 'name', 'product_set')