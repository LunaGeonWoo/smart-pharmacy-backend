from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyReviews.as_view()),
    path("<int:pk>", views.MyReviewDetail.as_view()),
]
