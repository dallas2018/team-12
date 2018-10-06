from django.db import models

# Create your models here.

class Current_Products(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='items_images',blank=True )
    condition = models.TextField()
    category = models.TextField()
    non_profit = models.TextField()
    price = models.TextField(default="0")


class Transactions(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    seller = models.TextField()
    buyer = models.TextField()
    price = models.TextField()
    non_profits = models.TextField()
