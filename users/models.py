from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
