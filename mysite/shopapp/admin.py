from django.contrib import admin

from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_updated', 'is_visible')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added', 'buyer')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
