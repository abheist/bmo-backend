from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'user'),
        (2, 'admin'),
        (3, 'superuser'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[0][0])
