from rest_framework import routers

from .views import ProductViewSet

products_router = routers.SimpleRouter()
products_router.register(r"products/product", ProductViewSet)
