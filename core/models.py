from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    card_id_number=models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'  # Important for AllAuth to recognize email as the login field
    REQUIRED_FIELDS = []

