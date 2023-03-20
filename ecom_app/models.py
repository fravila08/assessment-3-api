from django.db import models
from django.core import validators as v
from .validators import *

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, unique=True, blank=False, validators=[validate_acceptable_categories])
    
    def __str__(self):
        return f"{self.title}"
    
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.99, validators=[v.DecimalValidator(max_digits=10, decimal_places=2)])
    description = models.TextField(blank=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=[v.MinValueValidator(1)])

    def __str__(self):
        return f'{self.quantity}x {self.product.name} '