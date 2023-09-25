from rest_framework import serializers

from waretrack.products.models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "sku", "created_at"]

    created_at = serializers.SerializerMethodField()
    brand = BrandSerializer()
    category = CategorySerializer()

    def get_created_at(self, obj):
        return obj.created_at.strftime("%Y-%m-%d %H:%M")


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "brand",
            "category",
            "price",
            "weight",
            "is_active",
        ]

    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_null=True,
        required=False,
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["pk"] = instance.pk
        return representation
