from django.db import models
from core.models.mixins import AbstractBase, AccountTransaction
from core.models.user import User


class AllPermAccount(AbstractBase):
    # Can view, update, delete and add transactions to this account
    users = models.ManyToManyField(User, related_name="all_perm_accounts")


class AllPermTransaction(AccountTransaction):
    account = models.ForeignKey(
        AllPermAccount, on_delete=models.CASCADE, related_name="all_perm_transactions"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="all_perm_user_transactions",
        default=None,
    )

    class Meta:
        verbose_name = "All Perm Transaction"
        verbose_name_plural = "All Perm Transactions"
