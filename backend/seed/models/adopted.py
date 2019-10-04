"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class Adopted(Model):  #

    users = models.ManyToManyField('models.User', related_name='adopteds', blank=False,
        db_table = '_adopted__users')
    pets = models.ManyToManyField('models.Pet', related_name='adopteds', blank=False,
        db_table = '_adopted__pets')

    class Meta:
        db_table = '_adopted'
        app_label = 'models'
