import pytest

from waretrack.products.services.generate_sku import generate_sku


@pytest.mark.django_db
def test_generate_sku():
    # Given
    sku_length = 8
    # When
    sku = generate_sku(sku_length)
    # Then
    assert isinstance(sku, str)
    assert len(sku) == sku_length
