from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from core.models import User
from core.permissions import CreatePermission


class TestRegisterUser(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register-list")

    def test_register_user(self):
        data = {
            "email": "test@yopmail.com",
            "username": "test",
            "first_name": "test",
            "last_name": "user",
            "password": "p@55w0rd",
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data.get("access"))
        self.assertIsNotNone(response.data.get("refresh"))
        created_user = User.objects.get(email=data["email"])
        self.assertEqual(created_user.username, data["username"])
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
