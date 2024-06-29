from django.urls import path
from . import views

urlpatterns = [
    path("", views.Diagnosis.as_view()),
    path("<int:pk>", views.DiagnoseDetail.as_view()),
    path("history", views.DiagnoseHistory.as_view()),
]
