from django.urls import path
from .views import Inventories, InventoryDetail

urlpatterns = [
    path("", Inventories.as_view(), name="inventories_list"),
    path("<int:pk>", InventoryDetail.as_view(), name="inventory_detail"),
]
