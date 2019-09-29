from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Status
from .serializers import StatusSerialzer
# Create your views here.

class StatusListAPIView(APIView):
  permission_classes      = []
  authentication_classes  = []

  def get(self, request, format=None):
    allData = Status.objects.all()
    serializers = StatusSerialzer(allData, many=True)
    return Response(serializers.data)

class StatusDetailAPIView(APIView):
  permission_classes      = []
  authentication_classes  = []

  def get(self, request, id, format=None):
    data = Status.objects.get(pk=id)
    serializers = StatusSerialzer(data)
    return Response(serializers.data)