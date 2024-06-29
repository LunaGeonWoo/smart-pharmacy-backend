from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import Users, Me

urlpatterns = [
    path("", Users.as_view(), name="users_list"),
    path("me", Me.as_view(), name="user_detail"),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/verify", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
]
