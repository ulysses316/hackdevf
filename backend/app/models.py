"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_adopted():
    from seed.models.adopted import Adopted
    return Adopted

def get_chars():
    from seed.models.chars import Chars
    return Chars

def get_for_adoption():
    from seed.models.for_adoption import ForAdoption
    return ForAdoption

def get_media():
    from seed.models.media import Media
    return Media

def get_pet():
    from seed.models.pet import Pet
    return Pet

def get_raza():
    from seed.models.raza import Raza
    return Raza

def get_user():
    from seed.models.user import User
    return User

def get_file():
    from seed.models.helpers.file import File
    return File

Adopted = get_adopted()
Chars = get_chars()
ForAdoption = get_for_adoption()
Media = get_media()
Pet = get_pet()
Raza = get_raza()
User = get_user()
File = get_file()
