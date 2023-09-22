from django.contrib import admin

from waretrack.products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["sku", "created_at", "updated_at"]
    list_display = ["id", "name", "sku", "is_active"]
    search_fields = ["sku", "name"]
