"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from seed.helpers.viewsets import ViewSet

from app.models import Media
from app.serializers import MediaSerializer

class _MediaViewSet(ViewSet):  #

    serializer_class = MediaSerializer
    queryset = Media.objects.all()
