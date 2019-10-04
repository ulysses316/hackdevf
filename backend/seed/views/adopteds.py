"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Adopted
from app.serializers import AdoptedSerializer

class _AdoptedViewSet(ViewSet):  #

    serializer_class = AdoptedSerializer
    queryset = Adopted.objects.all()
