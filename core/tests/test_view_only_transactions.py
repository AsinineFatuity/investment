from django.urls import reverse
from rest_framework import status
from core.tests.fixtures.custom_test_case import CustomTestCase


class TestViewOnlyTransaction(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.view_only_transaction_url = reverse("view-only-list")

    def test_get_view_only_transaction(self):
        response = self.client.get(self.view_only_transaction_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_post_view_only_transaction(self):
        response = self.client.post(self.view_only_transaction_url)
        self.assertEqual(
            response.data.get("detail"),
            "You do not have permission to perform this action",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
