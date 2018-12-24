from django.shortcuts import render
from catalog.models import Product, Category

def product(request):
  return render(request, 'product.html')

def products(request):
  context = {
    'products': Product.objects.all()
  }
  return render(request, 'catalog/products.html', context)

def category(request, slug):
  category = Category.objects.get(slug=slug)
  context = {
    'current_category': category,
    'products': Product.objects.filter(category=category)
  }
  return render(request, 'catalog/category.html', context)
