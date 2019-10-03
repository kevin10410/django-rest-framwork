from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from django.shortcuts import get_object_or_404

from .models import Status
from .serializers import StatusSerialzer
# Create your views here.

class StatusListAPIView(
  generics.ListAPIView,
  CreateModelMixin,
  RetrieveModelMixin):
  permission_classes      = []
  authentication_classes  = []
  queryset                = Status.objects.all()
  serializer_class        = StatusSerialzer

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

  def get_queryset(self):
    return Status.objects.all()

  def get_object(self):
    request = self.request
    queryset = self.get_queryset()
    request_id = request.GET.get('id', None)
    return None if request_id == None else get_object_or_404(queryset, id=request_id)

  def get(self, request, *args, **kwargs):
    id = request.GET.get('id', None)
    if id is None:
      return super().get(request, *args, **kwargs)
    else:
      return self.retrieve(request, *args, **kwargs)


# class StatusDetailAPIView(DestroyModelMixin, UpdateModelMixin, generics.RetrieveUpdateDestroyAPIView):
class StatusDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
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