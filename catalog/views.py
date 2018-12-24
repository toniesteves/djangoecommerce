from django.shortcuts import render
from catalog.models import Product

def product(request):
  return render(request, 'product.html')

def products(request):
  context = {
  'products': Product.objects.all()
  }
  return render(request, 'catalog/products.html', context)
