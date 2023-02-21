from django.urls import path, include
from numpy import record
from .views import RecordList, RecordDetails

# record_list, record_details

urlpatterns = [
    path("records", RecordList.as_view()),
    path("records/<int:id>/", RecordDetails.as_view()),
    # path("records", record_list),
    # path("records/<int:pk>/", record_details),
]
