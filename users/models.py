from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    favorite_team = models.CharField(max_length=50, blank=True, null=True)
    favorite_city = models.CharField(max_length=50, blank=True, null=True)

