from http.client import HTTPResponse
from re import L
from django.shortcuts import render, HttpResponse
from .models import Record
from .serializers import RecordSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
@api_view(["GET", "POST"])
def record_list(request):
    if request.method == "GET":
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_RESQUEST)


@api_view(["GET", "PUT", "DELETE"])
def record_details(request, pk):
    try:
        record = Record.objects.get(pk=pk)

    except Record.DoesNotExist:
        return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = RecordSerializer(record)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = RecordSerializer(record, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
