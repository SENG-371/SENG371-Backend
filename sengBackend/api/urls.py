from django.urls import path, include
from numpy import record
from .views import record_list, record_details

urlpatterns = [
    path("records", record_list),
    path("records/<int:pk>/", record_details),
]
