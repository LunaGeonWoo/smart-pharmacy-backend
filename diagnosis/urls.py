from django.urls import path
from . import views

app_name = "diagnosis"

urlpatterns = [
    path("", views.Diagnosis.as_view(), name="diagnosis_list"),
    path("<int:pk>/", views.DiagnoseDetail.as_view(), name="diagnose_detail"),
    path("history/", views.DiagnoseHistory.as_view(), name="diagnose_history"),
]
