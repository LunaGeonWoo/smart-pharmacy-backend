from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from .serializers import InventorySerializer
from .models import Inventory


class Inventories(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_inventories = Inventory.objects.filter(owner=request.user)
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
            inventory = serializer.save(
                medicine=medicine,
                owner=request.user,
            )
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class InventoryDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise exceptions.NotFound

    def put(self, request, pk):
        inventory = self.get_object(pk)
        if inventory.owner != request.user:
            raise exceptions.PermissionDenied
        serializer = InventorySerializer(
            inventory,
            data=request.data,
        )
        if serializer.is_valid():
            inventory = serializer.save()
            serializer = InventorySerializer(inventory)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        inventory = self.get_object(pk)
        if inventory.owner != request.user:
            raise exceptions.PermissionDenied
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
