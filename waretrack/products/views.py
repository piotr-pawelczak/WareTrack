from waretrack.products.serializers import ProductSerializer
from waretrack.products.models import Product
from rest_framework import permissions, viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
