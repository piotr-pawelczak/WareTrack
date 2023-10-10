from django.db import models


class ShelfManager(models.Manager):
    def create(self, **shelf_data):
        warehouse_symbol = shelf_data.get("warehouse").symbol
        shelf_label = shelf_data.get("label")
        shelf_data["name"] = f"{warehouse_symbol}-{shelf_label}"
        return super().create(**shelf_data)


class LocationManager(models.Manager):
    def create(self, **location_data):
        shelf_name = location_data.get("shelf").name
        column_index = location_data.get("column_index")
        level_index = location_data.get("level_index")
        location_data["name"] = f"{shelf_name}-{column_index}-{level_index}"
        return super().create(**location_data)
