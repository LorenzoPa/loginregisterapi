from django.urls import path
from .views import RegisterView, LoginView, UpdateFavoriteTeamView, UpdateFavoriteCityView, MeView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("favorite/team/", UpdateFavoriteTeamView.as_view(), name="update-favorite"),
    path("favorite/city/", UpdateFavoriteCityView.as_view(), name="update-favorite"),

    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", MeView.as_view(), name="me"),

]
