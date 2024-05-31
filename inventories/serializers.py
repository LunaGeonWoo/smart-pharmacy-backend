from rest_framework.serializers import ModelSerializer
from .models import Inventory
from medicines.serializers import MedicineTinySerializer


class InventoriesSerializer(ModelSerializer):
    medicine = MedicineTinySerializer()

    class Meta:
        model = Inventory
        fields = (
            "id",
            "quantity",
            "medicine",
        )
