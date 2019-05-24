from django.contrib import admin
from .models import Brand, Category, Product, Attribute, ProductAttribute


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(ProductAttribute)
