from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Medicine


class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = (
            "name",
            "company",
            "price",
        )


class MedicineDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = "__all__"
