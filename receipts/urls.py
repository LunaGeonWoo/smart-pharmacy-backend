from django.urls import path
from . import views


urlpatterns = [
    path("", views.Receipts.as_view()),
    path("<int:pk>", views.ReceiptsDetail.as_view()),
]
