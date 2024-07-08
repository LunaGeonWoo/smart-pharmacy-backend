from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import Users, Me, LogIn, UserName

urlpatterns = [
    path("", Users.as_view(), name="signup"),
    path("username/<str:username>/", UserName.as_view(), name="username"),
    path("log-in/", LogIn.as_view(), name="login"),
    path("me/", Me.as_view(), name="me"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
