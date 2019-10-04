"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import ForAdoption
from app.models import User
from app.models import Pet
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _ForAdoptionSerializer(Serializer):  #
    
    users = DynamicRelationField('app.serializers.UserSerializer', 
        deferred=True, embed=True, many=True, read_only=True)
    pets = DynamicRelationField('app.serializers.PetSerializer', 
        deferred=True, embed=True, many=True, read_only=True)

    user_ids = serializers.PrimaryKeyRelatedField(many=True, source='users', queryset=User.objects.all(), 
        required=True, allow_null=False)
    pet_ids = serializers.PrimaryKeyRelatedField(many=True, source='pets', queryset=Pet.objects.all(), 
        required=True, allow_null=False)

    class Meta:
        model = ForAdoption
        fields = (
            'id',
            'hash',
            'users',
            'pets',
            'user_ids',
            'pet_ids',  
        )
