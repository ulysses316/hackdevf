"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Raza
from app.serializers import RazaSerializer

class _RazaViewSet(ViewSet):  #

    serializer_class = RazaSerializer
    queryset = Raza.objects.all()
