"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from seed.helpers.model import Model

class User(AbstractUser, Model):  #

    house_size = models.IntegerField(default=0)
    pet_number = models.IntegerField(default=0)
    city = models.CharField(max_length=70, blank=True)
    tel = models.IntegerField(default=0)
    facebook = models.CharField(max_length=70, blank=True)

    class Meta:
        db_table = '_user'
        app_label = 'models'
