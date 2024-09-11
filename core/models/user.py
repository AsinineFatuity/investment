from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models.mixins import AbstractBase
from enumchoicefield import EnumChoiceField


class RolesEnum(Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class User(AbstractBase, AbstractUser):
    # role maps
    ROLE_CHOICES_MAP = {
        RolesEnum.USER: "User",
        RolesEnum.ADMIN: "Admin",
    }
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    username = models.CharField(db_index=True, max_length=100, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    role = EnumChoiceField(RolesEnum, default=RolesEnum.USER)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
