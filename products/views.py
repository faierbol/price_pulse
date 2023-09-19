from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from . import permissions
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.ProductPermission,)
    filter_backend = [DjangoFilterBackend]
    filterset_fields = {
        "name": ["icontains"],
        "url": ["icontains"],
        "vendor": ["exact"],
    }
