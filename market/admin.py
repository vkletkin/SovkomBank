from django.contrib import admin
from .models import Product, Order


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "price")
    search_fields = ("pk", "name")
    list_filter = ("name", "price")
    empty_value_display = "-пусто-"


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("pk", "sale_date", "name", "quantity","total_price")
    search_fields = ("sale_date", "name")
    list_filter = ("sale_date", "name")
    empty_value_display = "-пусто-"

admin.site.register(Product, ProductsAdmin)
admin.site.register(Order, OrdersAdmin)
