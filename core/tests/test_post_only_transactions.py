from django.urls import reverse
from rest_framework import status
from core.tests.fixtures.custom_test_case import CustomTestCase
from core.models import PostOnlyTransaction


class TestViewOnlyTransaction(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.post_only_transaction_url = reverse("post-only-list")

    def test_create_post_only_transaction(self):
        data = {"amount": 1000, "date": "2024-09-01", "type": "D"}
        response = self.client.post(self.post_only_transaction_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PostOnlyTransaction.objects.count(), 1)
        created_transaction = PostOnlyTransaction.objects.first()
        self.assertEqual(created_transaction.amount, data["amount"])
        self.assertEqual(created_transaction.date.strftime("%Y-%m-%d"), data["date"])
        self.assertEqual(
            str(created_transaction.public_id).replace("-", ""), response.data["id"]
        )

    def test_get_post_only_transaction(self):
        response = self.client.get(self.post_only_transaction_url)
        self.assertEqual(
            response.data.get("detail"),
            "You do not have permission to perform this action",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
