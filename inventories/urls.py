from django.urls import path
from .views import Inventories, InventoryDetail, InventoriesPurchase

urlpatterns = [
    path("", Inventories.as_view(), name="inventories_list"),
    path("purchase/", InventoriesPurchase.as_view(), name="inventories_purchase"),
    path("<int:pk>/", InventoryDetail.as_view(), name="inventory_detail"),
]
