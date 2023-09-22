from django.urls import include, path
from rest_framework import routers

from waretrack.products.views import ProductViewSet

router = routers.SimpleRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [path("", include(router.urls))]
