"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_adopted_viewset():
    from seed.views.adopteds import _AdoptedViewSet
    return _AdoptedViewSet

def get_chars_viewset():
    from seed.views.charses import _CharsViewSet
    return _CharsViewSet

def get_for_adoption_viewset():
    from seed.views.for_adoptions import _ForAdoptionViewSet
    return _ForAdoptionViewSet

def get_media_viewset():
    from seed.views.mediaes import _MediaViewSet
    return _MediaViewSet

def get_pet_viewset():
    from seed.views.pets import _PetViewSet
    return _PetViewSet

def get_raza_viewset():
    from seed.views.razas import _RazaViewSet
    return _RazaViewSet

def get_user_viewset():
    from seed.views.users import _UserViewSet
    return _UserViewSet

def get_file_view():
    from seed.views.helpers.file import FileView
    return FileView

AdoptedViewSet = get_adopted_viewset()
CharsViewSet = get_chars_viewset()
ForAdoptionViewSet = get_for_adoption_viewset()
MediaViewSet = get_media_viewset()
PetViewSet = get_pet_viewset()
RazaViewSet = get_raza_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()