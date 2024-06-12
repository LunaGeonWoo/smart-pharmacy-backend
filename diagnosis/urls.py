from django.urls import path
from . import views

urlpatterns = [
    path("", views.Diagnose.as_view()),
    path("histories", views.DiagnoseHistories.as_view()),
    path("histories/<int:pk>", views.DiagnoseHistoryDetail.as_view()),
]
