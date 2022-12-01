from django.db import models
from django.contrib.auth.models import AbstractUser

class Things(AbstractUser):
    name = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
