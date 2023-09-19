from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Product

User = get_user_model()


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    vendor = factory.SubFactory("vendors.tests.factories.VendorFactory")
    name = factory.Faker("bs")
    price = factory.Faker(
        "pydecimal", left_digits=8, right_digits=2, min_value=None, max_value=None
    )
    url = factory.Faker("url")
    scraped_at = factory.Faker("date_time", tzinfo=timezone.utc)
