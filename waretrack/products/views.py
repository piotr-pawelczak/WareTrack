from rest_framework import permissions, viewsets

from waretrack.products.models import Brand, Category, Product
from waretrack.products.serializers import (
    BrandSerializer,
    CategorySerializer,
    ProductCreateSerializer,
    ProductSerializer,
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    default_serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    serializer_classes = {
        "create": ProductCreateSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.AllowAny]
