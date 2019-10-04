"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Pet
from app.serializers import PetSerializer

class _PetViewSet(ViewSet):  #

    serializer_class = PetSerializer
    queryset = Pet.objects.all()
