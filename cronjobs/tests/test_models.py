from django.test import TestCase

from ..models import Cronjob
from .factories import CronjobFactory


class CronjobTestCase(TestCase):
    def test_create_cronjob(self):
        """Test that Cronjob can be created using its factory."""

        obj = CronjobFactory()
        assert Cronjob.objects.all().get() == obj
