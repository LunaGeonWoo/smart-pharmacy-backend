from rest_framework.serializers import ModelSerializer
from .models import Inventory
from medicines.serializers import MedicineTinySerializer


class InventorySerializer(ModelSerializer):
    medicine = MedicineTinySerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = (
            "quantity",
            "medicine",
        )
