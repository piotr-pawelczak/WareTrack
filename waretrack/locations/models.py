from django.core.validators import MinValueValidator
from waretrack.locations.managers import ShelfManager, LocationManager
from django.db import models


class Warehouse(models.Model):
    class WarehouseType(models.IntegerChoices):
        DISTRIBUTION = 0, "Distribution Center"
        STORAGE = 1, "Storage Facility"
        RETAIL = 2, "Retail Store"
        MANUFACTURING = 3, "Manufacturing Plant"

    name = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=3, unique=True)
    address = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    warehouse_type = models.IntegerField(
        choices=WarehouseType.choices,
        default=WarehouseType.STORAGE,
    )

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Shelf(models.Model):
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="shelves",
    )
    label = models.CharField(max_length=10)
    columns = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    levels = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    name = models.CharField(unique=True, max_length=50, blank=True)
    is_active = models.BooleanField(default=True)

    objects = ShelfManager()

    class Meta:
        verbose_name_plural = "shelves"

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, related_name="locations")
    name = models.CharField(max_length=50)
    column_index = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    level_index = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    max_load = models.DecimalField(
        verbose_name="Max load [kg]",
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(1)],
    )
    is_active = models.BooleanField(default=True)

    objects = LocationManager()

    def __str__(self) -> str:
        return self.name
