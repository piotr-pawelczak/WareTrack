from django.urls import include, path
from rest_framework import routers

from waretrack.products.views import BrandViewSet, CategoryViewSet, ProductViewSet

appname = "products"

router = routers.SimpleRouter()
router.register(r"products", ProductViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"brands", BrandViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
