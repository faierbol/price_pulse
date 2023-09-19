from django.test import TestCase

from ..models import Vendor
from .factories import VendorFactory


class VendorTestCase(TestCase):
    def test_create_vendor(self):
        """Test that Vendor can be created using its factory."""

        obj = VendorFactory()
        assert Vendor.objects.all().get() == obj
