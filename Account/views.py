
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
    
    
# class LoginApiView(APIView):
#     permission_classes = [permissions.AllowAny]
    
    
#     serializer_class = LoginSerializer
#     def post(self, request):
#         data = request.data
#         print("data",data)
#         return Response({'data': data})
        
    
    

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
        