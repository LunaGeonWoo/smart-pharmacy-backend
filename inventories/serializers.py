from rest_framework.serializers import ModelSerializer
from .models import Inventory
from medicines.serializers import MedicineSerializer


class InventorySerializer(ModelSerializer):
    medicine = MedicineSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = (
            "pk",
            "quantity",
            "medicine",
        )
