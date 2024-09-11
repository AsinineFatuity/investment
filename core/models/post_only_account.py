from django.db import models
from core.models.mixins import AbstractBase
from core.models.user import User


class PostOnlyAccount(AbstractBase):
    users = models.ManyToManyField(User, related_name="post_only_accounts")
