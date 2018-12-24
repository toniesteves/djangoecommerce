# -*- coding: utf-8 -*-

from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.products, name='products'),
]
