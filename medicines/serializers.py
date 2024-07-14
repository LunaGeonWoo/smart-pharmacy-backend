from rest_framework import serializers
from .models import Medicine
from reviews.models import Review


class MedicineTinySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Medicine
        fields = (
            "id",
            "name",
            "company",
            "price",
            "average_rating",
            "review_count",
            "remaining",
        )

    def get_average_rating(self, medicine):
        return medicine.average_rating()

    def get_review_count(self, medicine):
        return medicine.review_count()


class MedicineDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medicine
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = (
            "id",
            "user",
            "medicine",
            "created_at",
        )


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"
