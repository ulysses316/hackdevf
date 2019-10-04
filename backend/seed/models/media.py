"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from datetime import datetime
from django.db import models
from seed.helpers.model import Model

class Media(Model):  #

    file_name = models.CharField(max_length=70, blank=True)
    url = models.CharField(max_length=70, blank=True)

    @property
    def user(self):
        return self.users.all()

    class Meta:
        db_table = '_media'
        app_label = 'models'
