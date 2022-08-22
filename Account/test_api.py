from .models import Profile
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class LoginTestCase(APITestCase):
    def setup(self):
        self.client = APIClient()
        self.email = "admin@gmail.com"
        self.password = "admin@123"
        user = Profile.objects.create(email=self.email, password=self.password)
        user.save()

    def test_empty_input(self):
        user_data = {"email": "", "password": ""}
        res = self.client.post(reverse("login"), user_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_incorrect_email_or_password(self):
        user_data = {"email": "admi@gmail.com", "password": "adin@123"}
        res = self.client.post(reverse("login"), user_data)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class TestRegisterApi(APITestCase):
    def test_to_check_for_empty_parameters(self):
        response = self.client.post(reverse("signup"))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_to_check_for_incomplete_data(self):
        sample_data = {
            "email": "me@mail.com",
            "password": "pass",
            "first_name": "Micah",
        }
        response = self.client.post(reverse("signup"), sample_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        