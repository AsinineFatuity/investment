from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from core.models import User
from core.permissions import CreatePermission


class TestUserAuthentication(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register-list")
        self.login_url = reverse("login-list")
        self.data = {
            "email": "test@yopmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "user",
            "password": "p@55w0rd",
        }

    def test_register_user(self):

        response = self.client.post(self.register_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get("access"))
        self.assertIsNotNone(response.data.get("refresh"))
        created_user = User.objects.get(email=self.data["email"])
        self.assertEqual(created_user.username, self.data["username"])
        self.assertEqual(
            created_user.groups.count(), len(CreatePermission.GRP_PERMS_MAP.keys())
        )
        user_permissions = created_user.get_all_permissions()
        self.assertNotEqual(user_permissions, set())
        expected_perms = set(
            [f"core.{perm}" for perm in CreatePermission.VIEW_ONLY_PERMISSIONS]
            + [f"core.{perm}" for perm in CreatePermission.POST_ONLY_PERMISSIONS]
            + [f"core.{perm}" for perm in CreatePermission.ALL_PERM_PERMISSIONS]
        )
        for perm in expected_perms:
            self.assertIn(perm, user_permissions)

    def test_user_login(self):
        response = self.client.post(self.register_url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        login_data = {
            "email": self.data["email"],
            "password": self.data["password"],
        }
        response = self.client.post(self.login_url, login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data.get("access"))
        self.assertIsNotNone(response.data.get("refresh"))
        self.assertEqual(response.data.get("user").get("email"), self.data["email"])
        self.assertEqual(
            response.data.get("user").get("username"), self.data["username"]
        )
        self.assertEqual(
            response.data.get("user").get("first_name"), self.data["first_name"]
        )
        self.assertEqual(
            response.data.get("user").get("last_name"), self.data["last_name"]
        )
        self.assertEqual(
            response.data.get("user").get("role"),
            User.ROLE_CHOICES_MAP.get(User.Role.USER),
        )
