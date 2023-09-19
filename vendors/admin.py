from django.contrib import admin

from .models import Vendor


class VendorAdmin(admin.ModelAdmin):
    model = Vendor
    list_display = [
        "name",
        "source",
        "geo_location",
        "parser_type",
        "cron_expression",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "name",
        "source",
        "geo_location",
        "parser_type",
        "cron_expression",
        "created_at",
        "updated_at",
    ]


admin.site.register(Vendor, VendorAdmin)
