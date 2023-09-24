import pytest
from rest_framework.reverse import reverse

from waretrack.products.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductViewSet:
    def test_list(self, api_client):
        # Given
        ProductFactory.create_batch(5)
        url = reverse("product-list")
        # When
        response = api_client.get(url)
        returned_data = response.json()
        # Then
        assert response.status_code == 200
        assert len(returned_data) == 5

    def test_detail(self, api_client):
        # Given
        product = ProductFactory.create()
        url = reverse("product-detail", args=[product.pk])
        # When
        response = api_client.get(url)
        # Then
        assert response.status_code == 200
        assert response.data["id"] == product.id

    def test_detail_product_not_found(self, api_client):
        # Given
        not_existing_pk = 100
        url = reverse("product-detail", args=[not_existing_pk])
        # When
        response = api_client.get(url)
        # Then
        assert response.status_code == 404
