from decimal import Decimal

from django.db import models


class Product(models.Model):
    vendor = models.ForeignKey(
        "vendors.Vendor",
        related_name="products",
        on_delete=models.CASCADE,
        null=False,
        help_text="Reference to Vendor",
    )
    name = models.CharField(
        max_length=255,
        null=False,
        help_text="Name of the product",
    )
    price = models.DecimalField(
        null=False,
        max_digits=10,
        decimal_places=2,
        help_text="Price of the product",
    )
    url = models.URLField(
        max_length=255,
        null=False,
        help_text="URL of the product on the vendor's site",
    )
    scraped_at = models.DateTimeField(
        null=False,
        help_text="Time when the product was last scraped",
    )

    def __str__(self):
        """String representation of a Product instance."""
        return self.name
