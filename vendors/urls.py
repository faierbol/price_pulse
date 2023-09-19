from rest_framework import routers

from .views import VendorViewSet

vendors_router = routers.SimpleRouter()
vendors_router.register(r"vendors/vendor", VendorViewSet)
