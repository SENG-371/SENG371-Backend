from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
def Index(request):
    return HttpResponse("works")
