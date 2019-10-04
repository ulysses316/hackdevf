"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from dynamic_rest.routers import DynamicRouter

from app.views import AdoptedViewSet
from app.views import CharsViewSet
from app.views import ForAdoptionViewSet
from app.views import MediaViewSet
from app.views import PetViewSet
from app.views import RazaViewSet
from app.views import UserViewSet
from app.views import FileView

router = DynamicRouter()
router.register(r'adopteds', AdoptedViewSet)
router.register(r'charses', CharsViewSet)
router.register(r'for_adoptions', ForAdoptionViewSet)
router.register(r'mediaes', MediaViewSet)
router.register(r'pets', PetViewSet)
router.register(r'razas', RazaViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]