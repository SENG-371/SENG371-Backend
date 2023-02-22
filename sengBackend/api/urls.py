from django.urls import include, path
from numpy import record
from rest_framework.routers import DefaultRouter

from .views import RecordViewSet, UserViewSet

router = DefaultRouter()
router.register("records", RecordViewSet, basename="records")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("api/", include(router.urls)),
]
