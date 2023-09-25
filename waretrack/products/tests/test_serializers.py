import datetime
from decimal import Decimal

import pytest

from waretrack.products.serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductCreateSerializer,
    ProductSerializer,
)
from waretrack.products.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductSerializer:
    def test_valid_data(self, product_payload):
        # Given
        serializer = ProductCreateSerializer(data=product_payload)
        assert serializer.is_valid()
        # When
        product = serializer.save()
        # Then
        assert product.name == product_payload["name"]
        assert product.description == product_payload["description"]
        assert product.price == Decimal(product_payload["price"])
        assert product.weight == Decimal(product_payload["weight"])
        assert product.is_active
        assert product.category.pk == product_payload["category"]
        assert product.brand.pk == product_payload["brand"]
        assert isinstance(product.sku, str)

    def test_empty_data(self):
        # Given
        empty_data = {}
        # When
        serializer = ProductSerializer(data=empty_data)
        # Then
        assert not serializer.is_valid()

    def test_invalid_price(self, product_payload):
        # Given
        product_payload["price"] = "-10.00"
        # When
        serializer = ProductSerializer(data=product_payload)
        # Then
        assert not serializer.is_valid()

    def test_invalid_weight(self, product_payload):
        # Given
        product_payload["weight"] = "-10.00"
        # When
        serializer = ProductSerializer(data=product_payload)
        # Then
        assert not serializer.is_valid()

    def test_deserialize_data(self):
        # Given
        product = ProductFactory.create()
        product.created_at = datetime.datetime(
            year=2023, month=2, day=20, hour=13, minute=30
        )
        # When
        serializer = ProductSerializer(product)
        data = serializer.data
        # Then
        assert data["id"] == product.id
        assert data["sku"] == product.sku
        assert data["created_at"] == "2023-02-20 13:30"
        assert data["category"] == CategorySerializer(product.category).data
        assert data["brand"] == BrandSerializer(product.brand).data

    def test_deserialize_multiple_instances(self):
        # Given
        products = ProductFactory.create_batch(2)
        # When
        serializer = ProductSerializer(products, many=True)
        # Then
        assert len(serializer.data) == 2
