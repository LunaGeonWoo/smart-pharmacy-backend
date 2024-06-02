from rest_framework import serializers
from .models import Review
from users.serializers import UserTinySerializers
from medicines.serializers import MedicineTinySerializer, MedicineDetailSerializer


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserTinySerializers(
        read_only=True,
    )

    class Meta:
        model = Review
        exclude = ("medicine",)


class MyReviewSerializer(serializers.ModelSerializer):
    medicine = MedicineTinySerializer(
        read_only=True,
    )

    class Meta:
        model = Review
        exclude = ("user",)
