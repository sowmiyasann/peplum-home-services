from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE = [

        ('customer', 'Customer'),

        ('provider', 'Provider')

    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE,
        default='customer'
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True
    )

    def __str__(self):

        return self.username
