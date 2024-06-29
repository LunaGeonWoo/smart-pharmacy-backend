from rest_framework import serializers
from .models import Diagnose, Query


class QueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = (
            "prompt",
            "result",
            "created_at",
        )


class DiagnosisDetailSerializer(serializers.ModelSerializer):
    queries = QueriesSerializer(many=True)

    class Meta:
        model = Diagnose
        fields = (
            "id",
            "title",
            "queries",
        )


class DiagnosisHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnose
        fields = (
            "id",
            "title",
            "created_at",
        )
