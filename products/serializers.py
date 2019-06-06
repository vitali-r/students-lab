from rest_framework import serializers
from products.models import (Category, Brand, Product, Attribute,
                             ProductAttribute)
from comments.serializers import CommentsSerializer
from users.serializers import UserSerializer


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('name',)


class ProductAttributeSerializer(serializers.ModelSerializer):
    attribute = AttributeSerializer()

    class Meta:
        model = ProductAttribute
        fields = (
            'id',
            'attribute',
            'value',
        )


class ProductSerializer(serializers.ModelSerializer):
    product_attributes = ProductAttributeSerializer(many=True, read_only=True)
    comments = CommentsSerializer(many=True)

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
            'product_attributes',
            'comments',
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
