from django.urls import path
from . import views

app_name = "receipts"

urlpatterns = [
    path("", views.Receipts.as_view(), name="receipts_list"),
    path("<int:pk>/", views.ReceiptsDetail.as_view(), name="receipt_detail"),
]
