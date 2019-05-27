from rest_framework import serializers
from products.models import (Category, Brand, Product, Attribute,
                             ProductAttribute)


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('id', 'name')


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = (
            'id',
            'attribute',
            'value',
        )


class ProductSerializer(serializers.ModelSerializer):
    product_attributes = ProductAttributeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'image',
            'brand',
            'category',
            'product_attributes'
        )


class BrandSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

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
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')
