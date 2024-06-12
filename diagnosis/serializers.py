from rest_framework import serializers
from .models import Diagnosis


class DiagnosisHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnosis
        fields = (
            "prompt",
            "created_at",
        )
