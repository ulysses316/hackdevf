"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from seed.helpers.model_admin import ModelAdminClass
from app.models import Adopted
from app.models import Chars
from app.models import ForAdoption
from app.models import Media
from app.models import Pet
from app.models import Raza
from app.models import User
from app.models import File

class _Admin:  #

  @staticmethod
  def register():  #
      
      class AdoptedAdmin(ModelAdminClass(Adopted)):
          pass
      
      class CharsAdmin(ModelAdminClass(Chars)):
          pass
      
      class ForAdoptionAdmin(ModelAdminClass(ForAdoption)):
          pass
      
      class MediaAdmin(ModelAdminClass(Media)):
          pass
      
      class PetAdmin(ModelAdminClass(Pet)):
          pass
      
      class RazaAdmin(ModelAdminClass(Raza)):
          pass
      
      class UserAdmin(ModelAdminClass(User)):
          pass
      
      class FileAdmin(ModelAdminClass(File)):
          pass
      admin.site.register(Adopted, AdoptedAdmin)
      admin.site.register(Chars, CharsAdmin)
      admin.site.register(ForAdoption, ForAdoptionAdmin)
      admin.site.register(Media, MediaAdmin)
      admin.site.register(Pet, PetAdmin)
      admin.site.register(Raza, RazaAdmin)
      admin.site.register(User, UserAdmin)
      admin.site.register(File, FileAdmin)
