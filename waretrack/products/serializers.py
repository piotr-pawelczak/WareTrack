from rest_framework import serializers
from waretrack.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sku', 'name', 'description', 'price', 'weight', 'created_at', 'is_active']
        read_only_fields = ['id', 'sku', 'created_at']
