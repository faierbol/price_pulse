from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Vendor

User = get_user_model()


class VendorFactory(DjangoModelFactory):
    class Meta:
        model = Vendor

    source = factory.Faker("bs")
    geo_location = factory.Faker("bs")
    parser_type = factory.Faker("bs")
    updated_at = factory.Faker("date_time", tzinfo=timezone.utc)
