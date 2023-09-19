from rest_framework import routers

from .views import CronjobViewSet

cronjobs_router = routers.SimpleRouter()
cronjobs_router.register(r"cronjobs/cronjob", CronjobViewSet)
