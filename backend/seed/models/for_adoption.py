"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class ForAdoption(Model):  #

    users = models.ManyToManyField('models.User', related_name='for_adoptions', blank=False,
        db_table = '_for_adoption__users')
    pets = models.ManyToManyField('models.Pet', related_name='for_adoptions', blank=False,
        db_table = '_for_adoption__pets')

    class Meta:
        db_table = '_for_adoption'
        app_label = 'models'
