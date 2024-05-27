from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Receipt


class ReceiptSerializer(ModelSerializer):

    class Meta:
        model = Receipt
        fields = (
            "id",
            "user",
            "medicine",
            "created_at",
        )


class ReceiptDetailSerialzier(ModelSerializer):

    class Meta:
        model = Receipt
        fields = "__all__"
