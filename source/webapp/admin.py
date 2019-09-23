from django.contrib import admin
from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', "description", "category", "price"]
    list_filter = ['name', 'category']
    list_display_links = ['pk', 'category']
    search_fields = ['name', 'category']
    fields = ['name', 'description', 'category', 'price', 'remainder']


admin.site.register(Product, ProductAdmin)
