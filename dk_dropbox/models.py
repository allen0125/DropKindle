from django.db import models
from django.conf import settings

# Create your models here.
class UserDropboxHistory(models.Model):
    dk_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dp_file_value = models.CharField(max_length=128)
    push_status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
