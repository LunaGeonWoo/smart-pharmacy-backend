from django.urls import path
from . import views

urlpatterns = [
    path("", views.Receipts.as_view(), name="receipts_list"),
    path("<int:pk>", views.ReceiptsDetail.as_view(), name="receipt_detail"),
]
