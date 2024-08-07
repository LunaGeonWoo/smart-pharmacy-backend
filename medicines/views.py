from django.db.models import Q
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ParseError
from rest_framework import status
from .serializers import MedicineTinySerializer, MedicineDetailSerializer
from .models import Medicine
from reviews.serializers import ReviewListSerializer
from reviews.models import Review
from favorites.models import Favorite


class Medicines(APIView):

    def get(self, request):

        try:
            page = int(request.query_params.get("page", 1))
            page_size = settings.PAGE_SIZE
            start = (page - 1) * page_size
            end = start + page_size
        except:
            return Response(
                {"error": "page must be >= 1"}, status=status.HTTP_400_BAD_REQUEST
            )
        search = request.query_params.get("search")
        if not search:
            medicines = Medicine.objects.all()[start:end]
            serializer = MedicineTinySerializer(
                medicines,
                many=True,
            )
        else:
            try:
                medicines = Medicine.objects.filter(
                    Q(name__contains=search)
                    | Q(company__contains=search)
                    | Q(main_ingredient__contains=search)
                    | Q(efficacy__contains=search)
                )[start:end]
                serializer = MedicineTinySerializer(
                    medicines,
                    many=True,
                )
            except:
                return Response(
                    {"error": "page must be >= 1"}, status=status.HTTP_400_BAD_REQUEST
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
        serializer = MedicineDetailSerializer(
            medicine,
            context={"request": request},
        )
        return Response(serializer.data)


class MedicineReviews(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = int(request.query_params.get("page", 1))
            page_size = settings.PAGE_SIZE
            start = (page - 1) * page_size
            end = start + page_size
            medicine = self.get_object(pk)
            all_reviews = Review.objects.filter(medicine=medicine)[start:end]
            serializer = ReviewListSerializer(
                all_reviews,
                many=True,
            )
        except:
            raise ParseError
        return Response(serializer.data)

    def post(self, request, pk):
        medicine = self.get_object(pk)
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid():
            review = serializer.save(
                user=request.user,
                medicine=medicine,
            )
            serializer = ReviewListSerializer(review)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MedicineFavorite(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        medicine = self.get_object(pk)
        if Favorite.objects.filter(user=request.user, medicine=medicine).exists():
            favorite = Favorite.objects.get(user=request.user, medicine=medicine)
            favorite.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            Favorite.objects.create(user=request.user, medicine=medicine)
            return Response(status=status.HTTP_201_CREATED)
