"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class Pet(Model):  #

    name = models.CharField(max_length=70, blank=True)
    ster = models.BooleanField(default=False)

    class Meta:
        db_table = '_pet'
        app_label = 'models'
