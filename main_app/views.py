from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

    # def __init__(self, name, longDescription,shortDescription, price, image):
    #     self.name = name
    #     self.longDescription = longDescription
    #     self.shortDescription = shortDescription
    #     self.price = price
    #     self.image = image

# products = [
#     Product('Football', 'Made for Americans Football', 'American Football', 60, 'image'),
#     Product('Baseball', 'Round white ball that is spherical', 'Standard baseball', 20, 'image'),
#     Product('Basketball', 'A sport for tall people', 'Knicks', 30, 'image'),
#     Product('Soccer', 'Used for the biggest sport in the world', 'White with Black dots', 40, 'image'),
# ]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def products_index(request):
    return render(request, 'products/index.html', {'products': products})