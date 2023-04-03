from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .models import Patients, Record, PatientRecord
from .serializers import (
    PatientSerializer,
    RecordSerializer,
    PatientRegistrationSerializer,
    RecordUpdateSerializer,
    PatientDeleteSerializer,
)
from django.shortcuts import get_object_or_404


class PatientDeleteView(APIView):
    serializer_class = PatientDeleteSerializer

    def delete(self, request, username):
        user = get_object_or_404(Patients, username=username)
        user.delete()
        return Response(
            {"message": "Patient deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class PatientList(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer


class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class PatientRegistrationView(generics.CreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientRegistrationSerializer


class PatientRecordsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        user = self.request.user
        return Patients.objects.filter(pk=user.pk)

    def post(self, request):
        serializer = PatientRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        user_records = request.data.get("user_records", [])
        PatientRecord.objects.filter(user=user).delete()
        for record_id in user_records:
            record = Record.objects.get(pk=record_id)
            user_record = PatientRecord(user=user, record=record)
            user_record.save()
        return Response(
            {
                "user": PatientSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User records updated successfully",
            }
        )


class RecordUpdateView(APIView):
    def put(self, request, pk):
        try:
            record = Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RecordUpdateSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
