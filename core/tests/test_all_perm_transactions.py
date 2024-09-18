from django.urls import reverse
from rest_framework import status
from core.tests.fixtures.custom_test_case import CustomTestCase
from core.models import AllPermTransaction


class TestAllPermTransaction(CustomTestCase):
    def setUp(self):
        super().setUp()
        self.all_perm_transaction_url = reverse("all-perm-list")
        self.data = {"amount": 1000, "date": "2024-09-01", "type": "D"}

    def test_create_all_perm_transaction(self):
        response = self.client.post(self.all_perm_transaction_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AllPermTransaction.objects.count(), 1)
        created_transaction = AllPermTransaction.objects.first()
        self.assertEqual(created_transaction.amount, self.data["amount"])
        self.assertEqual(
            created_transaction.date.strftime("%Y-%m-%d"), self.data["date"]
        )
        self.assertEqual(
            str(created_transaction.public_id).replace("-", ""), response.data["id"]
        )

    def test_update_all_perm_transaction(self):
        response = self.client.post(self.all_perm_transaction_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_transaction = AllPermTransaction.objects.first()
        update_data = {"amount": 2000, "date": "2024-09-02", "type": "W"}
        update_url = reverse("all-perm-detail", args=[created_transaction.public_id])
        response = self.client.put(update_url, data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        created_transaction.refresh_from_db()
        self.assertEqual(created_transaction.amount, update_data["amount"])
        self.assertEqual(
            created_transaction.date.strftime("%Y-%m-%d"), update_data["date"]
        )

    def test_read_all_perm_transaction(self):
        for _ in range(5):
            self.client.post(self.all_perm_transaction_url, data=self.data)
        response = self.client.get(self.all_perm_transaction_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_delete_all_perm_transaction(self):
        response = self.client.post(self.all_perm_transaction_url, data=self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_transaction = AllPermTransaction.objects.first()
        delete_url = reverse("all-perm-detail", args=[created_transaction.public_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AllPermTransaction.objects.count(), 0)
