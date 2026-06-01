from django.urls import path
from .import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MeView, PublicProfileView
urlpatterns = [
    path(
        "register/",
        views.RegisterView.as_view(),
        name="register-user"
    ),

    path(
        "login/",
        TokenObtainPairView.as_view(), 
        name="login"
    ),

    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh"
    ),

    path(
        "me/",
        MeView.as_view(),
        name="self-view"
    ),

    path(
        "<str:alias>/",
        PublicProfileView.as_view(),
        name="public-profile-view"
    )
]