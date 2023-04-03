from django.urls import path
from .views import (
    PatientList,
    PatientDetail,
    RecordList,
    RecordDetail,
    PatientRegistrationView,
    PatientRecordsView,
    RecordUpdateView,
    PatientDeleteView,
    PractitionerRegistrationView,
    PractitionerListView,
)

urlpatterns = [
    path("users/", PatientList.as_view()),
    path("practitioners/", PractitionerListView.as_view(), name="practitioner-list"),
    path("users/<int:pk>/", PatientDetail.as_view()),
    path("users/<int:pk>/records/", PatientRecordsView.as_view()),
    path("records/", RecordList.as_view()),
    path("records/<int:pk>/", RecordDetail.as_view()),
    path("users/register/", PatientRegistrationView.as_view()),
    path("practitioners/register/", PractitionerRegistrationView.as_view()),
    path("records/<int:pk>/update/", RecordUpdateView.as_view()),
    path(
        "users/delete/<str:username>/", PatientDeleteView.as_view(), name="user-delete"
    ),
]
