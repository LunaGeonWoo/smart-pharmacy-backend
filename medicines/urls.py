from django.urls import path
from . import views

urlpatterns = [
    path("", views.Medicines.as_view(), name="medicines_list"),
    path("<int:pk>/", views.MedicineDetail.as_view(), name="medicine_detail"),
    path("<int:pk>/reviews/", views.MedicineReviews.as_view(), name="medicine_reviews"),
]
