from django.urls import path
from . import views

urlpatterns = [
    path("", views.Medicine.as_view()),
]
