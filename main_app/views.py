from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView
from .models import Product, SubCart, Cart
from .forms import QuantityForm
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
    quantity_form = QuantityForm()
    return render(request, 'cart/index.html', {'carts': carts , 'quantity_form': quantity_form})

def cart_detail(request, cart_id):
  cart = SubCart.objects.get(id=cart_id)
  return render(request, 'cart/detail.html', {'cart': cart})

# def add_quantity(request, cart_id):
#   print('this string!!!!!!!!!!!')
#   print(request)
#   form = QuantityForm(request)
#   print(form)
#   if form.is_valid():
#     add_quantity = form.save(commit=False)
#     cart.quantity = add_quantity
#     cart.save()
#   return redirect('cart_detail', cart_id=cart_id)

class SubCartUpdate(UpdateView):
  model = SubCart
  fields = ['quantity']

class SubCartDelete(DeleteView):
  model = SubCart
  success_url = '/cart/'