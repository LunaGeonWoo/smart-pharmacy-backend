from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyReviews.as_view(), name="my_reviews"),
    path("<int:pk>/", views.MyReviewDetail.as_view(), name="my_review_detail"),
]
