from django.db import models
from django.contrib.auth.models import AbstractUser

class DKUser(AbstractUser):
    dropbox_token = models.CharField(max_length=128)
