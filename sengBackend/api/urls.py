from django.urls import include, path
from numpy import record
from rest_framework.routers import DefaultRouter

from .views import RecordViewSet

router = DefaultRouter()
router.register("records", RecordViewSet, basename="records")

urlpatterns = [
    path("", include(router.urls)),
]
