from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    longDescription = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name