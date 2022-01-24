from django.shortcuts import render
from .models import Product, SubCart, Cart
from django.http import HttpResponse
# Create your views here.


def home(request):
  return HttpResponse('<h1>Hello, Customer!</h1>')

def about(request):
  return render(request, 'about.html')

def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})

def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', {'product': product})

def cart_index(request):
    carts = SubCart.objects.all()
    return render(request, 'cart/index.html', {'carts': carts})

def cart_detail(request, cart_id):
  cart = SubCart.objects.get(id=cart_id)
  return render(request, 'cart/detail.html', {'cart': cart})