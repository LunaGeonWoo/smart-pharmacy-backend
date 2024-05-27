from rest_framework.views import APIView
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Receipt
from . import serializers


class Receipts(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_receipts = Receipt.objects.all()
        serializer = serializers.ReceiptSerializer(
            all_receipts,
            many=True,
        )
        return Response(serializer.data)


class ReceiptsDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Receipt.objects.get(pk=pk)
        except Receipt.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        receipt = self.get_object(pk)
        serializer = serializers.ReceiptDetailSerialzier(receipt)
        return Response(serializer.data)
