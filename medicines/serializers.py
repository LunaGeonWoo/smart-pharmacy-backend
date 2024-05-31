from rest_framework import serializers
from .models import Medicine
from reviews.models import Review


class MedicineTinySerializer(serializers.ModelSerializer):

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


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
