"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from seed.helpers.serializer import Serializer
from app.models import Media
from app.models import User
from app.models import File
from seed.serializers.helpers.file import FileSerializer

from dynamic_rest.fields import DynamicRelationField

class _MediaSerializer(Serializer):  #
    
    user = DynamicRelationField('app.serializers.UserSerializer',source='users',deferred=True, embed=True, many=True, read_only=True)

    user_ids = serializers.PrimaryKeyRelatedField(many=True, source='users', read_only=True)

    class Meta:
        model = Media
        fields = (
            'id',
            'hash',
            'file_name',
            'url',
            'user',
            'user_ids',  
        )
