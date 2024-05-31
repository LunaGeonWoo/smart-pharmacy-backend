from rest_framework import serializers
from .models import Receipt
from medicines.serializers import MedicineDetailSerializer


class ReceiptSerializer(serializers.ModelSerializer):
    medicine = serializers.SerializerMethodField()

    class Meta:
        model = Receipt
        fields = (
            "id",
            "medicine",
            "quantity",
            "purchase_at",
        )

    def get_medicine(self, receipt):
        return receipt.medicine.name


class ReceiptDetailSerializer(serializers.ModelSerializer):

    medicine = MedicineDetailSerializer()

    class Meta:
        model = Receipt
        exclude = ("owner",)
