from django.conf import settings
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from .serializers import MyReviewSerializer
from .models import Review


class MyReviews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            page_size = settings.PAGE_SIZE
            start = (page - 1) * page_size
            end = start + page_size
            my_reviews = Review.objects.filter(user=request.user)[start:end]
            serializer = MyReviewSerializer(
                my_reviews,
                many=True,
            )
        except:
            return redirect(f"{request.path}?page=1")
        return Response(serializer.data)


class MyReviewDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise exceptions.NotFound

    def put(self, request, pk):
        my_review = self.get_object(pk)
        if my_review.user != request.user:
            raise exceptions.PermissionDenied
        serializer = MyReviewSerializer(
            my_review,
            data=request.data,
        )
        if serializer.is_valid():
            my_review = serializer.save()
            serializer = MyReviewSerializer(my_review)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        my_review = self.get_object(pk)
        if my_review.user != request.user:
            raise exceptions.PermissionDenied
        my_review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
