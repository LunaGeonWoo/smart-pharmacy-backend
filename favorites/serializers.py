from rest_framework import serializers
from medicines.serializers import MedicineTinySerializer
from .models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    medicine = MedicineTinySerializer()

    class Meta:
        model = Favorite
        fields = ("medicine",)
