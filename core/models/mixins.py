import uuid
from django.db import models
from django.utils import timezone
from enum import Enum
from enumchoicefield import EnumChoiceField


class PublicIdentifier(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class AuditTimeStamp(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        abstract = True


class AbstractBase(AuditTimeStamp, PublicIdentifier):
    class Meta:
        abstract = True


class TransactionTypeEnum(Enum):
    D = "DEPOSIT"
    W = "WITHDRAWAL"


class AccountTransaction(AbstractBase):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = EnumChoiceField(TransactionTypeEnum)
    transaction_ts = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Account Transaction"
        verbose_name_plural = "Account Transactions"
        abstract = True
