from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        max_length=150,
        editable=False,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
