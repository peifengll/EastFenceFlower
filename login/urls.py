#!/user/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from libs.utils.jwtSerializer import MyTokenObtainPairView
from login.views import TestView

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("test/", TestView.as_view(), name="token_refresh"),
]
