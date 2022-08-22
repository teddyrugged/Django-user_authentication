from django.urls import path
from .views import(CustomTokenPairView,RegisterApiView)
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    # path("login/",CustomTokenPairView.as_view(),name="login"),
    path("signup/",RegisterApiView.as_view(),name="signup"),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]