import factory

from waretrack.locations.models import Location, Shelf, Warehouse


class WarehouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Warehouse

    name = factory.Sequence(lambda n: "Test Warehouse %d" % n)
    symbol = factory.Sequence(lambda n: chr(65 + (n % 26)) + chr(65 + ((n + 1) % 26)))
    description = factory.Faker("paragraph", nb_sentences=3)
    address = factory.Faker("address")


class ShelfFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Shelf

    warehouse = factory.SubFactory(WarehouseFactory)
    label = factory.Sequence(lambda n: chr(65 + (n % 26)))


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location

    shelf = factory.SubFactory(ShelfFactory)
    max_load = factory.fuzzy.FuzzyDecimal(low=0, high=1000, precision=2)
