from django.conf import settings
from django.shortcuts import redirect

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from . import serializers
from .models import Review
from .serializers import ReviewSerializer, ReviewDetailSerializer


# user id filter해서 내가 쓴 리뷰만 가져오고, 페이지 추가
class MyReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
            page_size = settings.PAGE_SIZE
            start = (page - 1) * page_size
            end = start + page_size
            my_reviews = Review.objects.filter(user=request.user)[start:end]
            serializer = serializers.ReviewSerializer(
                my_reviews,
                many=True,
            )
        except:
            return redirect(f"{request.path}?page=1")
        return Response(serializer.data)


# 리뷰 내용 다 보여주고 수정, 삭제
class MyReviewsDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_reviews(self, request, pk):
        try:
            return Review.objects.filter(user=request.user).get(pk=pk)
        except Review.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        my_reviews = self.get_reviews(pk)
        serializer = serializers.ReviewDetailSerializer(my_reviews)
        return Response(serializer.data)
