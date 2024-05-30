from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Receipt
from medicines.models import Medicine
from medicines.serializers import MedicineDetailSerializer


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = (
            "id",
            "user",
            "medicine",
            "created_at",
        )


class ReceiptDetailSerializer(serializers.ModelSerializer):

    medicine = MedicineDetailSerializer()

    class Meta:
        model = Receipt
        fields = "__all__"
