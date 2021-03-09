from django.contrib import admin
from django.urls import path, include
from stocks import views

urlpatterns = [
    path('list_items/', views.list_items, name='list_items'),
    path('add_items/', views.add_items, name='add_items'),
]