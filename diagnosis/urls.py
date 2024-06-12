from django.urls import path
from . import views

urlpatterns = [
    path("", views.Diagnose.as_view()),
    path("histories", views.DiagnoseHistory.as_view()),
]
