from django.contrib import admin
from django.urls import path, include
from .views import notification

urlpatterns = [
    path('notification/', notification, name='notification')
]