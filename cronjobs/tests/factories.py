from datetime import timezone

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from ..models import Cronjob

User = get_user_model()


class CronjobFactory(DjangoModelFactory):
    class Meta:
        model = Cronjob

    task_name = factory.Faker("bs")
    cron_expression = factory.Faker("bs")
    updated_at = factory.Faker("date_time", tzinfo=timezone.utc)

    @factory.post_generation
    def vendors(self, create, extracted, **kwargs):
        if not create:
            return
        # if related model instances are provided, add them to the relation
        if extracted:
            for model in extracted:
                self.vendors.add(model)
        # by default the relation is empty
