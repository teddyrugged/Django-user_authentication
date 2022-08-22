
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from .models import Profile
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
class RegisterApiView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    
