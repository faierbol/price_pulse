from rest_framework import serializers

from .models import Cronjob


class CronjobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cronjob
        fields = [
            "id",
            "vendors",
            "task_name",
            "cron_expression",
            "enabled",
            "created_at",
            "updated_at",
        ]
