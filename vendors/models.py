from datetime import date

from django.db import models
from django.utils.timezone import now


class Vendor(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        default="",
        help_text="Name of the vendor",
    )
    source = models.CharField(
        max_length=255,
        null=False,
        help_text='Source type (e.g., "universal_ecommerce")',
    )
    geo_location = models.CharField(
        max_length=255,
        null=False,
        help_text='Geographical location (e.g., "Romania")',
    )
    parser_type = models.CharField(
        max_length=255,
        null=False,
        help_text='Parser type (e.g., "ecommerce_product")',
    )
    cron_expression = models.CharField(
        max_length=255,
        null=False,
        default="NULL",
        help_text="Cron expression for scheduling",
    )
    created_at = models.DateTimeField(
        null=False,
        default=now,
        help_text="Record creation time",
    )
    updated_at = models.DateTimeField(
        null=False,
        help_text="Record update time",
    )

    def __str__(self):
        """String representation of a Vendor instance."""
        return self.name
