import uuid
from django.db import models
from django.utils import timezone


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
