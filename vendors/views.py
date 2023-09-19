from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
from .models import Vendor
from .serializers import VendorSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = (permissions.VendorPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "cron_expression": ["icontains"],
    }
