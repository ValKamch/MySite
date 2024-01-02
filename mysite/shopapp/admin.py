from typing import Any
from django.contrib import admin
from django.db.models import QuerySet
from django.http.request import HttpRequest

from .models import Product, Order
from .admin_mixin import ExportAsCSVMixin

#В продуктах отображать в какие заказы входит
class OrderInline(admin.StackedInline):
    model = Product.orders.through

# Групповые действия
@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)

@admin.action(description="Unarchive products")
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    actions = [
        mark_archived,
        mark_unarchived,
        "export_csv",
    ]
    inlines = [
        OrderInline,
    ]
    #list_display = "pk", "name", "description", "price", "discount"
    list_display = "pk", "name", "description_short", "price", "discount", "archived"   #Что показываем
    list_display_links = "pk", "name"                                       #По каким полях открывакм детали
    ordering = "-pk",                                                       #Порядок
    search_fields = "name", "description"                                   #Поиск
    fieldsets = [                                                           #Группировка полей в деталях
        (None, {
            "fields": ("name", "description")
        }),
        ("Price option", {
            "fields": ("price", "discount"),
#            "classes": ("collapse",),                                      #Сворачивает группу полей
#            "classes": ("wide",),                                           #Поля немного правее
            "classes": ("wide", "collapse"),                                #Можно совмещать
        }),
        ("Extra options", {
            "fields": ("archived",),
            "classes": ("collapse"),
            "description": "Extra options. Field 'archived' is for soft delete",
            
        }),
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."

#Для отображения связанных деталей заказа
#Две строки - разные способы отражения
#class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]
    list_display = "delivery_address", "promocode", "created_at", "user_verbose"

#Что бы не делать множественные запросы по user и по продуктам
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return Order.objects.select_related("user").prefetch_related("products")
    
#Если хочу форматировать возвращаемое значение поля
    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username    





#admin.site.register(Product, ProductAdmin)
