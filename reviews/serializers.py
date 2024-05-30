from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Review


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
