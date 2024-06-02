from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            "id",
            "medicine",
            "created_at",
        )


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
