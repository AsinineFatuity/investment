from django.urls import reverse
from rest_framework import status
from core.tests.fixtures.custom_test_case import CustomTestCase
from django.test import tag


class TestAdminQueryTransactions(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.admin_query_transaction_url = reverse("admin-query-list")

    @tag("rel")
    def test_non_admin_user_cannot_query_transactions(self):
        response = self.client.get(self.admin_query_transaction_url)
        self.assertEqual(
            str(response.data["detail"]),
            "You do not have permission to perform this action.",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_admin_query_transaction(self):
        response = self.client.get(self.admin_query_transaction_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])
