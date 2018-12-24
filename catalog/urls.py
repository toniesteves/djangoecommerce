# -*- coding: utf-8 -*-

from django.urls import path, re_path
from . import views

app_name = 'catalog'

urlpatterns = [
  path('', views.products, name='products'),
  re_path(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
  re_path(r'^products/(?P<slug>[\w_-]+)/$', views.product, name='product')
]
