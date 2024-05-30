from django.urls import path
from . import views

urlpatterns = [
    path("", views.Medicines.as_view()),
    path("<int:pk>", views.MedicineDetail.as_view()),
    path("reviews/", views.Reviews.as_view()),
    path("reviews/<int:pk>/", views.ReviewDetail.as_view()),
]
