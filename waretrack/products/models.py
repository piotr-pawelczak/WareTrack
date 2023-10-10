from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from waretrack.products.services.generate_sku import generate_sku


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self) -> str:
        return self.name


class ProductManager(models.Manager):
    def create(self, **product_data):
        product_data["sku"] = generate_sku(length=8)
        return super().create(**product_data)


class Product(models.Model):
    sku = models.CharField(
        max_length=8, unique=True, db_index=True, blank=True, null=True
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
    category = TreeForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    weight = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    objects = ProductManager()

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sku} - {self.name}"
