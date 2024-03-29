from django.contrib import admin
from django.urls import path, include
from .views import product

urlpatterns = [
    path('product/', product, name='product')
]