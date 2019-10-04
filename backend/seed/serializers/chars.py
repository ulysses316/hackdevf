"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Chars
from app.models import Pet
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _CharsSerializer(Serializer):  #
    
    pet = DynamicRelationField('app.serializers.PetSerializer',source='pets',deferred=True, embed=True, many=True, read_only=True)

    pet_ids = serializers.PrimaryKeyRelatedField(many=True, source='pets', read_only=True)

    class Meta:
        model = Chars
        fields = (
            'id',
            'hash',
            'size',
            'weight',
            'color',
            'pet',
            'pet_ids',  
        )
