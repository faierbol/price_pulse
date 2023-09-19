from django.contrib import admin

from .models import Cronjob


class CronjobAdmin(admin.ModelAdmin):
    model = Cronjob
    list_display = [
        "task_name",
        "cron_expression",
        "enabled",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "task_name",
        "cron_expression",
        "enabled",
        "created_at",
        "updated_at",
    ]


admin.site.register(Cronjob, CronjobAdmin)
