from django.test import TestCase

from ..models import Product
from .factories import ProductFactory


class ProductTestCase(TestCase):
    def test_create_product(self):
        """Test that Product can be created using its factory."""

        obj = ProductFactory()
        assert Product.objects.all().get() == obj
