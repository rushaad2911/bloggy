# apps/user/urls.py

from django.urls import path, include
from .views import CustomSignupView

urlpatterns = [
    path("signup/", CustomSignupView.as_view(), name="account_signup"),
    path("", include("allauth.urls")),
]
