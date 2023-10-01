import pytest

from waretrack.locations.tests.factories import (
    LocationFactory,
    ShelfFactory,
    WarehouseFactory,
)


class TestWarehouse:
    pass


@pytest.mark.django_db
class TestShelf:
    def test_generate_name(self):
        warehouse = WarehouseFactory.create(symbol="WA")
        shelf = ShelfFactory.create(label="A", warehouse=warehouse)
        assert shelf.name == "WA-A"


@pytest.mark.django_db
class TestLocation:
    def test_generate_name(self):
        warehouse = WarehouseFactory.create(symbol="WA")
        shelf = ShelfFactory.create(warehouse=warehouse, label="A")
        location = LocationFactory.create(shelf=shelf, column_index=1, level_index=1)
        assert location.name == "WA-A-1-1"
