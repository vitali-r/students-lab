from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.

class Comment(models.Model):
    FIVE = '5' 
    FOUR = '4' 
    THREE = '3' 
    TWO = '2' 
    ONE = '1' 
    MARK_CHOICES = ( (FIVE, '5'), (FOUR, '4'), (THREE, '3'), (TWO, '2'), (ONE, '1') ) 
    text = models.TextField(verbose_name='Text')
    mark = models.CharField(max_length=1, verbose_name='Mark', choices=MARK_CHOICES, default=FIVE)
    user_id = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return "Comment on product - {}, added by user - {}".format(self.product_id, self.user_id)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
