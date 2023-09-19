from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
from .models import Cronjob
from .serializers import CronjobSerializer


class CronjobViewSet(viewsets.ModelViewSet):
    queryset = Cronjob.objects.all()
    serializer_class = CronjobSerializer
    permission_classes = (permissions.CronjobPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "cron_expression": ["icontains"],
        "task_name": ["icontains"],
    }
