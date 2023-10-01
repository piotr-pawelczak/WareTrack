from django.contrib import admin

from waretrack.locations.models import Location, Shelf, Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "symbol", "is_active"]
    search_fields = ["name", "symbol"]


@admin.register(Shelf)
class ShelfAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
    search_fields = ["name"]
    readonly_fields = ["name"]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active"]
    search_fields = ["name"]
    readonly_fields = ["name"]
