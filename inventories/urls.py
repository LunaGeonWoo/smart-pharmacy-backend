from django.urls import path
from .views import Inventories

urlpatterns = [
    path("", Inventories.as_view()),
]
