from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    HAIR_CHOICES = (
     ('hair1', 'Hair Style 1'),
     ('hair2', 'Hair Style 2'),
    )

    hair = models.CharField(max_length=100, choices=HAIR_CHOICES, default='hair1')
