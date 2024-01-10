from typing import Any
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .forms import ProductForm, GroupForm
from .models import Product, Order, ProductImage

class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse: 
        products = [
            ('laptop', 1999),
            ('Desktop', 2999)
        ]
        context = {
            "products": products,
        }
        return render(request, 'shopapp/shop-index.html', context=context)

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),
        }
        return render(request, 'shopapp/groups-list.html', context=context)
    
    def post(self, request:HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)
        
class ProductDetailView(DetailView):
    template_name = 'shopapp/product-detail.html'
#    model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = 'product'
    
    
class ProductsListView(ListView): 
    template_name = 'shopapp/products-list.html'
    #model = Product
    context_object_name = 'products'
    queryset = Product.objects.filter(archived=False)
    

class ProductCreateView(UserPassesTestMixin, CreateView):  
    def test_func(self):
        # return self.request.user.groups.filter(name="secret-group").exits()
        return self.request.user.is_superuser
    model = Product
#Если указывать здесь поля, то класс в форме не нужен  
#    form_class =  ProductForm     
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy("shopapp:products_list")

class ProductUpdateView(UpdateView):
    model = Product  
#    fields = "name", "price", "description", "discount", "preview"
    #template_name = "product_update_form"
    form_class = ProductForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse(
            "shopapp:product_detail", 
            kwargs={"pk": self.object.pk},
        )

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image,
            )
        return response          
                         


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("shopapp:products_list")
# Если нужно не удалить, а поставить признак удаления

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
        

class OrderListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects.select_related("user").prefetch_related("products").all()
    )


def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related("user").prefetch_related("products").all(),
    }
    return render(request, 'shopapp/order-list.html', context=context)

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "shopapp.view_order"
    queryset = (
        Order.objects.select_related("user").prefetch_related("products").all()
    )