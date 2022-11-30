from django.db import models
from app.models import Category 
from app.models import Product
from app.models import Customer


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=45)
    qty =models.FloatField()
    total =models.FloatField()