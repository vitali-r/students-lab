from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.

class Comment(models.Model):
    MARK_CHOICES = ( ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1') )
    text = models.TextField(verbose_name='Text')
    mark = models.CharField(max_length=1, verbose_name='Mark', choices=MARK_CHOICES)
    user_id = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"