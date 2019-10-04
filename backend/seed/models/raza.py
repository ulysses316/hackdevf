"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class Raza(Model):  #

    raza = models.CharField(max_length=70, blank=True)

    @property
    def pet(self):
        return self.pets.all()

    class Meta:
        db_table = '_raza'
        app_label = 'models'
