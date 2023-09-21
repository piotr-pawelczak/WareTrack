from django.db import models
from waretrack.products.services.generate_sku import generate_sku


class Product(models.Model):

    SKU_LENGTH = 8

    sku = models.CharField(max_length=SKU_LENGTH, unique=True, db_index=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sku} - {self.name}"

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = generate_sku(self.SKU_LENGTH)
        super().save(*args, **kwargs)
