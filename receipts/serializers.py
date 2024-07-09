from rest_framework import serializers
from .models import Receipt, PastMedicine
from medicines.serializers import MedicineTinySerializer


class ReceiptSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Receipt
        fields = (
            "id",
            "total_price",
            "purchase_at",
        )

    def get_total_price(self, receipt):
        return receipt.total_price()


class PastMedicineSerializer(serializers.ModelSerializer):
    medicine = MedicineTinySerializer()

    class Meta:
        model = PastMedicine
        fields = (
            "quantity",
            "price_per_medicine_at_purchase",
            "medicine",
        )


class ReceiptDetailSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    past_medicines = PastMedicineSerializer(many=True)

    class Meta:
        model = Receipt
        fields = (
            "purchase_at",
            "total_price",
            "past_medicines",
        )

    def get_total_price(self, receipt):
        return receipt.total_price()
