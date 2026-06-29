from django.db import models
from django.contrib.auth.models import AbstractUser


class User(
AbstractUser
):

    ROLE=[

('customer','Customer'),

('provider','Provider')

]

    role=models.CharField(
        max_length=30,
        choices=ROLE
    )

    phone=models.CharField(
        max_length=20
    )
