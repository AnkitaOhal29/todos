from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = (
        ('User', 'User'),
        ('Admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='User')
