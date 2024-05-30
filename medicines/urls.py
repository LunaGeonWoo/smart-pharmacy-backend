from django.urls import path
from . import views

urlpatterns = [
    path("", views.Medicines.as_view()),
    path("<int:pk>", views.MedicineDetail.as_view()),
    path("<int:pk>/reviews/", views.Reviews.as_view()),
    path("<int:pk2>/reviews/<int:pk>/", views.ReviewDetail.as_view()),
]
