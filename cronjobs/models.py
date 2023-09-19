from datetime import date

from django.db import models
from django.utils.timezone import now


class Cronjob(models.Model):
    vendors = models.ManyToManyField(
        "vendors.Vendor",
        related_name="cronjobs",
        blank=True,
        help_text="References to multiple Vendors",
    )
    task_name = models.CharField(
        max_length=255,
        null=False,
        help_text="Name of the task to run",
    )
    cron_expression = models.CharField(
        max_length=255,
        null=False,
        help_text="Cron expression for scheduling",
    )
    enabled = models.BooleanField(
        null=False,
        default=True,
        help_text="Whether the cron job is enabled",
    )
    created_at = models.DateTimeField(
        null=False,
        default=now,
        help_text="	Record creation time",
    )
    updated_at = models.DateTimeField(
        null=False,
        help_text="Record update time",
    )

    def __str__(self):
        """String representation of a Cronjob instance."""
        return self.task_name
