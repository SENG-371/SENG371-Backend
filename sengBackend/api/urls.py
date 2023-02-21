from django.urls import path, include
from numpy import record
from .views import RecordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("records", RecordViewSet, basename="records")

urlpatterns = [
    path("", include(router.urls)),
]
