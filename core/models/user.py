from enum import Enum
from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models.mixins import AbstractBase
from enumchoicefield import EnumChoiceField
from phonenumber_field.modelfields import PhoneNumberField


class RolesEnum(Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class GenderEnum(Enum):
    M = "MALE"
    F = "FEMALE"


class User(AbstractBase, AbstractUser):
    # gender maps
    GENDER_CHOICES_MAP = {GenderEnum.M: "Male", GenderEnum.F: "Female"}
    # role maps
    ROLE_CHOICES_MAP = {
        RolesEnum.USER: "User",
        RolesEnum.ADMIN: "Admin",
    }
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    username = models.CharField(db_index=True, max_length=100, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = EnumChoiceField(GenderEnum, default=GenderEnum.M)
    address = models.CharField(max_length=100, null=True, blank=True)
    role = EnumChoiceField(RolesEnum, default=RolesEnum.USER)
    phone_number = PhoneNumberField(default="")

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
