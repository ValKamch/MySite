from django.contrib.auth.models import Group
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Product, Order

def shop_index(request: HttpRequest):
    products = [
        ('laptop', 1999),
        ('Desktop', 2999)
    ]
    context = {
        "products": products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)

def groups_list(request: HttpRequest):
    context = {
        "groups": Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)

def products_list(request: HttpRequest):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/products-list.html', context=context)

def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/order-list.html', context=context)
