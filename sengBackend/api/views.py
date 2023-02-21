from http.client import HTTPResponse

from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import APIView, api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Record
from .serializers import RecordSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    authentication_classes = (TokenAuthentication,)


# class RecordList(
#     generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin
# ):
#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     # def get(self, request):
#     #     records = Record.objects.all()
#     #     serializer = RecordSerializer(records, many=True)
#     #     return Response(serializer.data)

#     # def post(self, request):
#     #     serializer = RecordSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_RESQUEST)


# class RecordDetails(
#     generics.GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
# ):

#     queryset = Record.objects.all()
#     serializer_class = RecordSerializer

#     lookup_field = "id"

#     def get(self, request, id):
#         return self.retrieve(request, id=id)

#     def put(self, request, id):
#         return self.update(request, id=id)

#     def delete(self, request, id):
#         return self.destroy(request, id=id)

#     # def get_object(self, id):
#     #     try:
#     #         return Record.objects.get(id=id)

#     #     except Record.DoesNotExist:
#     #         return HTTPResponse(status=status.HTTP_404_NOT_FOUND)

#     # def get(self, request, id):
#     #     record = self.get_object(id)
#     #     serializer = RecordSerializer(record)
#     #     return Response(serializer.data)

#     # def put(self, request, id):
#     #     record = self.get_object(id)
#     #     serializer = RecordSerializer(record, data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     # def delete(self, request, id):
#     #     record = self.get_object(id)
#     #     record.delete()
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
