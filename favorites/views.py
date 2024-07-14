from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Favorite
from .serializers import FavoriteSerializer


class Favorites(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(
            my_favorites,
            many=True,
        )
        return Response(serializer.data)
