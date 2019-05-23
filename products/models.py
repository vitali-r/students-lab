from django.db import models


class Category(models.Model): 
    name = models.CharField(max_length=50, unique=True) 

    def __str__(self): 
        return self.name 


class Brand(models.Model): 
    name = models.CharField(max_length=50, unique=True) 
    description = models.TextField() 
    image = models.ImageField(upload_to='photos/brands', verbose_name='Brand`s photo') 

    def __str__(self): 
        return self.name 


class Product(models.Model): 
    WHITE = 'Wh' 
    BLACK = 'Bl' 
    RED = 'Re' 
    GRAY = 'Gr' 
    PINK = 'Pi' 
    COLOR_CHOICES = [ 
        (WHITE, 'Wh'), 
        (BLACK, 'Bl'), 
        (RED, 'Re'), 
        (GRAY, 'Gr'), 
        (PINK, 'Pi'), 
    ] 
    name = models.CharField(max_length=50) 
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2) 
    description = models.TextField() 
    discount = models.PositiveIntegerField(default=0) 
    ram = models.PositiveIntegerField(blank=True)  # Random Access Memory
    color = models.CharField( 
        max_length = 2, 
        choices = COLOR_CHOICES, 
        default = WHITE 
    ) 
    image = models.ImageField(upload_to='photos/products', verbose_name='Product`s photo') 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE) 

    def __str__(self): 
        return self.name
