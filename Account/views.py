
from rest_framework import permissions
from .models import Profile
from .serializers import RegistrationSerializer, CustomTokenObtainPairSerializer
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]

class RegisterApiView(CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]
    


# class 
# if request.method == 'POST':
#     serializer = RegistrationSerializer(data = request.data)
#     data = {}
#     if serializer.is_valid():
#         account = serializer.save()
#         data['response'] = 'succesfully register a new user.'
#         data['first_name'] = account.first_name
#         data['last_name'] = account.last_name
#         data['email'] = account.email
#     else:
#         data.serializer.errors
# # return Response('data')
        