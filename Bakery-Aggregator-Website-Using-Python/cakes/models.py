# models.py

from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cake(models.Model):
    name  = models.CharField(max_length=200)
    weight = models.CharField(max_length=200, default=None)
    description = models.CharField(max_length=500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2083, default=False)
    cake_available = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    bakery_name = models.CharField(max_length=200, null=True)  # New field for bakery name

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    address = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.name}"

class PinCode(models.Model):
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.code
