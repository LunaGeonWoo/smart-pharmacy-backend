from rest_framework import serializers
from .models import Diagnosis


class DiagnosisHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnosis
        fields = (
            "id",
            "prompt",
            "created_at",
        )


class DiagnosisHistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        exclude = (
            "updated_at",
            "user",
        )
