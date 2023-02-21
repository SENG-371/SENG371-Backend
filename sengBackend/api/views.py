from http.client import HTTPResponse
from re import L
from django.shortcuts import render, HttpResponse
from .models import Record
from .serializers import RecordSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def record_list(request):
    if request.method == "GET":
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def record_details(request, pk):
    try:
        record = Record.objects.get(pk=pk)

    except Record.DoesNotExist:
        return HTTPResponse(status=404)

    if request.method == "GET":
        serializer = RecordSerializer(record)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = RecordSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        record.delete()
        return HTTPResponse(status=204)
