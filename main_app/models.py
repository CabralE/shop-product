from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    longDescription = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'product_id': self.id})

class SubCart(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE) 
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('cart_index')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('product', 'cart'), name='once_per_product_cart')
        ]
        
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through=SubCart)

