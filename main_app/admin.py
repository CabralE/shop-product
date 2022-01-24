from django.contrib import admin
from .models import Product, SubCart, Cart
# Register your models here.

admin.site.register(Product)
admin.site.register(SubCart)
admin.site.register(Cart)