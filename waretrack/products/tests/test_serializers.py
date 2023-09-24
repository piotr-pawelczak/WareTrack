import datetime
from decimal import Decimal

import pytest

from waretrack.products.serializers import ProductSerializer
from waretrack.products.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductSerializer:
    def setup_class(self):
        self.valid_data = {
            "name": "Test Product",
            "description": "Test Product description",
            "price": "100.00",
            "weight": "10.4",
        }

    def test_valid_data(self):
        # Given
        serializer = ProductSerializer(data=self.valid_data)
        assert serializer.is_valid()
        # When
        product = serializer.save()
        # Then
        assert product.name == "Test Product"
        assert product.description == "Test Product description"
        assert product.price == Decimal("100.00")
        assert product.weight == Decimal("10.4")
        assert product.is_active
        assert isinstance(product.sku, str)

    def test_empty_data(self):
        # Given
        empty_data = {}
        # When
        serializer = ProductSerializer(data=empty_data)
        # Then
        assert not serializer.is_valid()

    def test_invalid_price(self):
        # Given
        invalid_price_data = self.valid_data
        invalid_price_data["price"] = "-10.00"
        # When
        serializer = ProductSerializer(data=invalid_price_data)
        # Then
        assert not serializer.is_valid()

    def test_invalid_weight(self):
        # Given
        invalid_weight_data = self.valid_data
        invalid_weight_data["weight"] = "-10.00"
        # When
        serializer = ProductSerializer(data=invalid_weight_data)
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

    def test_deserialize_multiple_instances(self):
        # Given
        products = ProductFactory.create_batch(2)
        # When
        serializer = ProductSerializer(products, many=True)
        # Then
        assert len(serializer.data) == 2
