"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_adopted_serializer():
    from seed.serializers.adopted import _AdoptedSerializer
    return _AdoptedSerializer

def get_chars_serializer():
    from seed.serializers.chars import _CharsSerializer
    return _CharsSerializer

def get_for_adoption_serializer():
    from seed.serializers.for_adoption import _ForAdoptionSerializer
    return _ForAdoptionSerializer

def get_media_serializer():
    from seed.serializers.media import _MediaSerializer
    return _MediaSerializer

def get_pet_serializer():
    from seed.serializers.pet import _PetSerializer
    return _PetSerializer

def get_raza_serializer():
    from seed.serializers.raza import _RazaSerializer
    return _RazaSerializer

def get_user_serializer():
    from seed.serializers.user import _UserSerializer
    return _UserSerializer

def get_file_serializer():
    from seed.serializers.helpers.file import FileSerializer
    return FileSerializer

AdoptedSerializer = get_adopted_serializer()
CharsSerializer = get_chars_serializer()
ForAdoptionSerializer = get_for_adoption_serializer()
MediaSerializer = get_media_serializer()
PetSerializer = get_pet_serializer()
RazaSerializer = get_raza_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()
