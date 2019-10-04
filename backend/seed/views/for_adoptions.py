"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import ForAdoption
from app.serializers import ForAdoptionSerializer

class _ForAdoptionViewSet(ViewSet):  #

    serializer_class = ForAdoptionSerializer
    queryset = ForAdoption.objects.all()
