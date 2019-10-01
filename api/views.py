from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import Status
from .serializers import StatusSerialzer
# Create your views here.

class StatusListAPIView(CreateModelMixin, generics.ListAPIView):
  permission_classes      = []
  authentication_classes  = []
  queryset                = Status.objects.all()
  serializer_class        = StatusSerialzer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  # def get(self, request, format=None):
  #   allData = Status.objects.all()
  #   serializers = StatusSerialzer(allData, many=True)
  #   return Response(serializers.data)

class StatusDetailAPIView(DestroyModelMixin, UpdateModelMixin, generics.RetrieveAPIView):
  permission_classes      = []
  authentication_classes  = []
  queryset                = Status.objects.all()
  serializer_class        = StatusSerialzer

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

  # def get(self, request, id, format=None):
  #   data = Status.objects.get(pk=id)
  #   serializers = StatusSerialzer(data)
  #   return Response(serializers.data)


class StatusCreateAPIView(generics.CreateAPIView):
  permission_classes      = []
  authentication_classes  = []
  queryset                = Status.objects.all()
  serializer_class        = StatusSerialzer



class StatusUpdateAPIView(generics.UpdateAPIView):
  permission_classes      = []
  authentication_classes  = []
  queryset                = Status.objects.all()
  serializer_class        = StatusSerialzer


class StatusDeleteAPIView(generics.DestroyAPIView):
  permission_classes      = []
  authentication_classes  = []
  queryset                = Status.objects.all()
  serializer_class        = StatusSerialzer