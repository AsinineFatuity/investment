from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from core.models.user import User


class CustomTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register-list")
        self.data = {
            "email": "test@yopmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "user",
            "password": "p@55w0rd",
        }
        register_response = self.client.post(self.register_url, self.data)
        self.assertEqual(register_response.status_code, status.HTTP_201_CREATED)
        self.user = User.objects.get(email=self.data["email"])
        self.client.force_authenticate(user=self.user)
