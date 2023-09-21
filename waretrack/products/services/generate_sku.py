import random
import string


def generate_sku(length: int) -> str:
    from waretrack.products.models import Product
    while True:
        sku = ''.join(
            random.choices(string.ascii_uppercase + string.digits, k=length)
        )
        if not Product.objects.filter(sku=sku).exists():
            return sku
