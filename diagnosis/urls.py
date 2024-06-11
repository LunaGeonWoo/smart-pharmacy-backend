from django.urls import path
from . import views

urlpatterns = [
    path("", views.Diagnosis.as_view()),
]
