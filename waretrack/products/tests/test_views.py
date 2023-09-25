import pytest

from waretrack.products.models import Product
from waretrack.products.tests.factories import ProductFactory


@pytest.mark.django_db
class TestProductViewSet:
    def test_list(self, api_client):
        # Given
        ProductFactory.create_batch(5)
        url = "/api/products/"
        # When
        response = api_client.get(url)
        returned_data = response.json()
        # Then
        assert response.status_code == 200
        assert len(returned_data) == 5

    def test_detail(self, api_client):
        # Given
        product = ProductFactory.create()
        url = f"/api/products/{product.pk}/"
        # When
        response = api_client.get(url)
        # Then
        assert response.status_code == 200
        assert response.data["id"] == product.id

    def test_detail_product_not_found(self, api_client):
        # Given
        not_existing_pk = 100
        url = f"/api/products/{not_existing_pk}/"
        # When
        response = api_client.get(url)
        # Then
        assert response.status_code == 404

    def test_create(self, api_client, product_payload):
        # Given
        url = "/api/products/"
        assert not Product.objects.count()
        # When
        response = api_client.post(url, product_payload)
        product = Product.objects.last()
        # Then
        assert response.status_code == 201
        assert Product.objects.count() == 1
        assert product.name == product_payload["name"]

    def test_create_with_empty_data(self, api_client):
        # Given
        url = "/api/products/"
        empty_data = {}
        assert not Product.objects.count()
        # When
        response = api_client.post(url, empty_data)
        # Then
        assert response.status_code == 400
        assert not Product.objects.count()

    def test_create_invalid_price(self, api_client, product_payload):
        # Given
        invalid_price = "-5.00"
        url = "/api/products/"
        product_payload["price"] = invalid_price
        assert not Product.objects.count()
        # When
        response = api_client.post(url, product_payload)
        # Then
        assert response.status_code == 400
        assert not Product.objects.count()

    def test_create_invalid_weight(self, api_client, product_payload):
        # Given
        invalid_weight = "-5.00"
        url = "/api/products/"
        product_payload["weight"] = invalid_weight
        assert not Product.objects.count()
        # When
        response = api_client.post(url, product_payload)
        # Then
        assert response.status_code == 400
        assert not Product.objects.count()

    def test_create_allow_empty_category(self, api_client, product_payload):
        # Given
        url = "/api/products/"
        product_payload["category"] = ""
        assert Product.objects.count() == 0
        # When
        response = api_client.post(url, product_payload)
        product_pk = response.json()["pk"]
        product = Product.objects.get(pk=product_pk)
        # Then
        assert response.status_code == 201
        assert Product.objects.count() == 1
        assert product.category is None
