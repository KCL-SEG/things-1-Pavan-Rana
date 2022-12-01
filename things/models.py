from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Thing(models.Model):
    REQUIRED_FIELDS = ('quantity',)
    USERNAME_FIELD = 'name'
    is_anonymous = False
    is_authenticated = True

    name = models.CharField(unique=True,blank=False,max_length=30)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
