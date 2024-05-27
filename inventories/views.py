from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class Inventories(APIView):
    authentication_classes = [IsAuthenticated]

    def get(self, pk):
        pass
