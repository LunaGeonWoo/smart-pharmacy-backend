from rest_framework.views import APIView
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import exceptions
from .models import Receipt
from . import serializers


class Receipts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_receipts = Receipt.objects.filter(owner=request.user)
        serializer = serializers.ReceiptSerializer(
            my_receipts,
            many=True,
        )
        return Response(serializer.data)


class ReceiptsDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Receipt.objects.get(pk=pk)
        except Receipt.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, pk):
        receipt = self.get_object(pk)
        if receipt.owner != request.user:
            raise exceptions.PermissionDenied
        serializer = serializers.ReceiptDetailSerializer(receipt)
        return Response(serializer.data)
