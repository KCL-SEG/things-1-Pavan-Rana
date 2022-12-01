from django.db import models.Model
from django.contrib.auth.models import AbstractUser

class Thing(Model):
    name = models.TextField(unique=True,blank=False,max_length=30)
    description = models.TextField(max_length=120)
    quantity = models.IntegerField()
