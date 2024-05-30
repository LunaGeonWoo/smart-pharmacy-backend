from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory
from medicines.models import Medicine


class Inventories(APIView):
    permission_classes = [IsAuthenticated]

    def get_medicine(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request):
        my_inventories = Inventory.objects.filter(
            owner=request.user,
        )
        serializer = InventorySerializer(
            my_inventories,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            try:
                medicine_pk = int(request.data.get("medicine"))
            except:
                raise exceptions.ParseError
            medicine = self.get_medicine(medicine_pk)
            inventory = serializer.save(medicine=medicine, owner=request.user)
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
