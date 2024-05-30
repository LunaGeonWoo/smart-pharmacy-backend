from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Medicine
from reviews.serializers import *
from reviews.models import Review


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


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            "user",
            "medicine",
            "created_at",
        )


class ReviewDetailSerialzier(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
