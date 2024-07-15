from rest_framework import serializers
from .models import Medicine
from favorites.models import Favorite


class MedicineTinySerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Medicine
        fields = (
            "id",
            "name",
            "company",
            "img_url",
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
    average_rating = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Medicine
        fields = "__all__"

    def get_average_rating(self, medicine):
        return medicine.average_rating()

    def get_review_count(self, medicine):
        return medicine.review_count()

    def get_is_favorite(self, medicine):
        request = self.context["request"]
        if request.user.is_authenticated:
            return Favorite.objects.filter(
                user=request.user,
                medicine=medicine,
            ).exists()
        return False
