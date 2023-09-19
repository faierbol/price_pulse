from rest_framework import serializers

from .models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = [
            "id",
            "name",
            "source",
            "geo_location",
            "parser_type",
            "cron_expression",
            "created_at",
            "updated_at",
        ]
