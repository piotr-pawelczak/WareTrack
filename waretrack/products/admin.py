from django.contrib import admin

from waretrack.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
