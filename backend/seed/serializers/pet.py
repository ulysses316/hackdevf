"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Pet
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _PetSerializer(Serializer):  #

    class Meta:
        model = Pet
        fields = (
            'id',
            'hash',
            'name',
            'ster',  
        )
