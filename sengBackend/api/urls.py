from django.urls import path
from .views import (
    UserList,
    UserDetail,
    RecordList,
    RecordDetail,
    UserRegistrationView,
    UserRecordsView,
    RecordUpdateView,
    UserDeleteView,
)

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()),
    path("users/<int:pk>/records/", UserRecordsView.as_view()),
    path("records/", RecordList.as_view()),
    path("records/<int:pk>/", RecordDetail.as_view()),
    path("users/register/", UserRegistrationView.as_view()),
    path("records/<int:pk>/update/", RecordUpdateView.as_view()),
    path("users/delete/<str:username>/", UserDeleteView.as_view(), name="user-delete"),
]
