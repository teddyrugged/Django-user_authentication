from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from account.models import Account
from account.serializers import AccountSerializer
from rest_framework.response import Response





# class 
if request.method == 'POST':
    serializer = RegistrationSerializer(data = request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'succesfully register a new user.'
        data['first_name'] = account.first_name
        data['last_name'] = account.last_name
        data['email'] = account.email
    else:
        data.serializer.errors
# return Response('data')
        