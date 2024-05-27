from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Medicine
from . import serializers


class Medicines(APIView):

    def get(self, request):
        all_medicines = Medicine.objects.all()
        serializer = serializers.MedicineSerializer(
            all_medicines,
            many=True,
        )
        return Response(serializer.data)


class MedicineDetail(APIView):

    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        medicine = self.get_object(pk)
        serializer = serializers.MedicineSerializer(medicine)
        return Response(serializer.data)
