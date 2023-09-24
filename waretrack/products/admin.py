from django.contrib import admin

from waretrack.products.models import Brand, Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["sku", "created_at", "updated_at"]
    list_display = ["id", "name", "sku", "is_active"]
    search_fields = ["sku", "name"]


admin.site.register(Category)
admin.site.register(Brand)
