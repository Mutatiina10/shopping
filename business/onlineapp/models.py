from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    product_description = models.TextField()
    product_category = models.CharField(max_length=100)
    product_comment = models.TextField(max_length=100)
    product_image = models.ImageField(upload_to='images/')
    product_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.product_name 