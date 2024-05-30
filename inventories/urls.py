from django.urls import path
from .views import Inventories, InventoryDetail

urlpatterns = [
    path("", Inventories.as_view()),
    path("<int:pk>", InventoryDetail.as_view()),
]
