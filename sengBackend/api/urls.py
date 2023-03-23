from django.urls import include, path
from numpy import record
from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UserList, UserDetail, RecordList, RecordDetail, UserRegistrationView

urlpatterns = [
    path("users/", UserList.as_view(), name="user_list"),
    path("users/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("records/", RecordList.as_view(), name="record_list"),
    path("records/<int:pk>/", RecordDetail.as_view(), name="record_detail"),
    path("register/", UserRegistrationView.as_view(), name="user_registration"),
]
