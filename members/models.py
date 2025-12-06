from django.db import models
from django.contrib.auth.models import AbstractUser
from members.managers import CustomUserManager
class Member(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.TextField(max_length=15, blank=True, null=True)
    USERNAME_FIELD = 'email' #use email instead of username
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email