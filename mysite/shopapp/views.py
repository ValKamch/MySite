from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpRequest

from .forms import ProductForm
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

def create_product(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():  
            #name = form.cleaned_data["name"]
            #price = form.cleaned_data["price"]
            #Product.objects.create(**form.cleaned_data)      
            form.save()
            url = reverse("shopapp:products_list")
            return redirect(url)
    else:
        form = ProductForm()
    context = {
        "form": form,
    }
    
    return render(request, "shopapp/create-product.html", context=context)


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/order-list.html', context=context)
