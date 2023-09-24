import factory
from factory.fuzzy import FuzzyDecimal

from waretrack.products.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda n: "Category %d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: "Brand %d" % n)


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Sequence(lambda n: "Test Product %d" % n)
    description = factory.Faker("paragraph", nb_sentences=3)
    category = factory.SubFactory(CategoryFactory)
    brand = factory.SubFactory(BrandFactory)
    price = FuzzyDecimal(low=0, high=1000, precision=2)
    weight = FuzzyDecimal(low=0, high=100, precision=2)
    is_active = factory.Faker("pybool")
