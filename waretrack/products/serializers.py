from rest_framework import serializers

from waretrack.products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "sku",
            "name",
            "description",
            "price",
            "weight",
            "created_at",
            "is_active",
        ]
        read_only_fields = ["id", "sku", "created_at"]

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M")
