from rest_framework.serializers import ModelSerializer
from .models import Inventory


class InventoriesSerializer(ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            "pk",
            "quantity",
            "medicine",
        )
