from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Your custom fields here

    # Add a related_name argument to groups and user_permissions fields
    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        related_name='customuser_set'  # Change 'customuser_set' to your preferred name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        related_name='customuser_set'  # Change 'customuser_set' to your preferred name
    )
