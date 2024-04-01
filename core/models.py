from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass




class UOM(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
            return self.name

