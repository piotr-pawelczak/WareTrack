import pytest
from rest_framework.test import APIClient

from waretrack.products.tests.factories import BrandFactory, CategoryFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def product_payload():
    category = CategoryFactory.create()
    brand = BrandFactory.create()
    payload = {
        "name": "Test Product",
        "description": "Test Product description",
        "price": "100.00",
        "weight": "10.4",
        "category": category.pk,
        "brand": brand.pk,
    }
    return payload
