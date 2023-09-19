from cronjobs.urls import cronjobs_router
from django.contrib import admin
from django.urls import include, path
from products.urls import products_router
from rest_framework import routers
from vendors.urls import vendors_router

from users.urls import users_router

router = routers.DefaultRouter()
router.registry.extend(cronjobs_router.registry)
router.registry.extend(products_router.registry)
router.registry.extend(vendors_router.registry)
router.registry.extend(users_router.registry)

urlpatterns = [
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    path("api/docs/auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/v1/", include("openapi.urls")),
    path("api/v1/", include(router.urls)),
]
