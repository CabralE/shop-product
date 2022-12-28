from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .models import Product, SubCart, Cart
from .forms import QuantityForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.http import HttpResponse
# Create your views here.


def home(request):
  return render(request, 'base.html')

def about(request):
  return render(request, 'about.html')


def products_index(request):
    products = Product.objects.all()
    return render(request, 'products/index.html', {'products': products})


def products_detail(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'products/detail.html', {'product': product})

@login_required
def purchase(request):
  carts = SubCart.objects.filter(user_id=request.user.id)
  carts.delete()
  return redirect('index')
  

@login_required
def purchase_checkout(request):
  carts = SubCart.objects.filter(user_id=request.user.id)
  quantity_form = QuantityForm()
  total = 0
  for cart in carts:
    total += cart.product.price * cart.quantity

  print(total)
  return render(request, 'checkout/index.html', {'carts': carts, 'quantity_form': quantity_form, 'total': total})

@login_required
def cart_index(request):
    carts = SubCart.objects.filter(user_id=request.user.id)
    quantity_form = QuantityForm()
    return render(request, 'cart/index.html', {'carts': carts , 'quantity_form': quantity_form})

@login_required
def cart_detail(request, cart_id):
  print(cart_id)
  cart = SubCart.objects.get(id=cart_id)
  return render(request, 'cart/detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
  # product = Product.objects.get(id=product_id)
  # cart, created = Cart.objects.get_or_create(user_id=request.user)
  # subcart, created = SubCart.objects.get_or_create(product = product, cart=cart, quantity=1, user_id=request.user)
  # if not created:
  #   subcart.quantity = subcart.quantity + 1
  #   subcart.save()
  # return redirect('index')
  product = Product.objects.get(id=product_id)
  cart = Cart.objects.get_or_create(user_id=request.user)
  exists = SubCart.objects.filter(product = product, cart=cart, quantity=1, user_id=request.user).exists()
  if exists == True:
    return redirect('index')
  else:
    subcart = SubCart(product = product, cart=cart, quantity=1, user_id=request.user)
    subcart.save()
    return redirect('index')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      Cart.objects.create(user=user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)




class SubCartUpdate(LoginRequiredMixin, UpdateView):
  model = SubCart
  fields = ['quantity']



class SubCartDelete(LoginRequiredMixin, DeleteView):
  model = SubCart
  success_url = '/cart/'

class SubCartCreate(LoginRequiredMixin, CreateView):
  model = SubCart
  fields = ['quantity']
  success_url = '/cart/'

  # def form_valid(self,form):
  #   form.instance.user = self.request.user
  #   return super().form_valid(form)


