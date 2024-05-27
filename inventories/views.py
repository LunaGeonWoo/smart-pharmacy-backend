from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import InventoriesSerializer
from .models import Inventory


class Inventories(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_inventories = Inventory.objects.filter(owner=request.user)
        serializer = InventoriesSerializer(
            my_inventories,
            many=True,
        )
        return Response(serializer.data)
