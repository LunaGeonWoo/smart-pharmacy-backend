from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Medicine
from . import serializers
from reviews.serializers import ReviewSerializer, ReviewDetailSerialzier
from reviews.models import Review


class Medicines(APIView):

    def get(self, request):
        all_medicines = Medicine.objects.all()
        serializer = serializers.MedicineSerializer(
            all_medicines,
            many=True,
        )
        return Response(serializer.data)


class MedicineDetail(APIView):

    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        medicine = self.get_object(pk)
        serializer = serializers.MedicineDetailSerializer(medicine)
        return Response(serializer.data)


class Reviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_reviews = Review.objects.all()
        serializer = serializers.ReviewSerializer(
            all_reviews,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
            )
            serializer = ReviewSerializer(review)
            return Response(serializer.data)


class ReviewDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = serializers.ReviewDetailSerialzier(review)
        return Response(serializer.data)
