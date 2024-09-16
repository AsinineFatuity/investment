from django.db import models
from core.models.mixins import AbstractBase, AccountTransaction
from core.models.user import User


class ViewOnlyAccount(AbstractBase):
    # Can only view transactions in this account
    users = models.ManyToManyField(User, related_name="view_only_accounts")


class ViewOnlyTransaction(AccountTransaction):
    account = models.ForeignKey(
        ViewOnlyAccount, on_delete=models.CASCADE, related_name="view_only_transactions"
    )

    class Meta:
        verbose_name = "View Only Transaction"
        verbose_name_plural = "View Only Transactions"
