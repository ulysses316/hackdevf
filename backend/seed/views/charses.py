"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Chars
from app.serializers import CharsSerializer

class _CharsViewSet(ViewSet):  #

    serializer_class = CharsSerializer
    queryset = Chars.objects.all()
