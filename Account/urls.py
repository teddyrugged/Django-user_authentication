from django.urls import path
from .views import(CustomTokenPairView,RegisterApiView)


urlpatterns = [
    path("login/",CustomTokenPairView.as_view(),name="login"),
    path("signup/",RegisterApiView.as_view(),name="signup")
]