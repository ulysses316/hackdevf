"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
import re
from django.db.models import Q
from graphene_django.types import DjangoObjectType
from app.models import Adopted as AdoptedModel
from app.models import Chars as CharsModel
from app.models import ForAdoption as ForAdoptionModel
from app.models import Media as MediaModel
from app.models import Pet as PetModel
from app.models import Raza as RazaModel
from app.models import User as UserModel
from app.models import File as FileModel

def query(data, model):
    data = data.replace(".", "__")
    data = data.replace("(", "")
    data = data.replace(")", "")
    res = Q()
    queries = [i.strip() for i in data.split("OR")]
    for q in queries:
        filters = [i.strip() for i in q.split("AND")]
        values = {}
        for f in filters:
            ele = f.split("=")
            values[ele[0].strip()] = ele[1].strip()
        res |= Q(**values)
    return model.objects.filter(res)

class Adopted(DjangoObjectType):
    class Meta:
        model = AdoptedModel

class Chars(DjangoObjectType):
    class Meta:
        model = CharsModel

class ForAdoption(DjangoObjectType):
    class Meta:
        model = ForAdoptionModel

class Media(DjangoObjectType):
    class Meta:
        model = MediaModel

class Pet(DjangoObjectType):
    class Meta:
        model = PetModel

class Raza(DjangoObjectType):
    class Meta:
        model = RazaModel

class User(DjangoObjectType):
    class Meta:
        model = UserModel
        exclude = ('password',)
class File(DjangoObjectType):
    class Meta:
        model = FileModel

class Query(object):
    
    adopteds = graphene.List(Adopted, query=graphene.String())
    adopted = graphene.Field(Adopted, id=graphene.Int())
    charses = graphene.List(Chars, query=graphene.String())
    chars = graphene.Field(Chars, id=graphene.Int())
    forAdoptions = graphene.List(ForAdoption, query=graphene.String())
    forAdoption = graphene.Field(ForAdoption, id=graphene.Int())
    mediaes = graphene.List(Media, query=graphene.String())
    media = graphene.Field(Media, id=graphene.Int())
    pets = graphene.List(Pet, query=graphene.String())
    pet = graphene.Field(Pet, id=graphene.Int())
    razas = graphene.List(Raza, query=graphene.String())
    raza = graphene.Field(Raza, id=graphene.Int())
    users = graphene.List(User, query=graphene.String())
    user = graphene.Field(User, id=graphene.Int())
    files = graphene.List(File, query=graphene.String())
    file = graphene.Field(File, id=graphene.Int())

    def resolve_adopteds(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], AdoptedModel)
        return AdoptedModel.objects.all()
    def resolve_adopted(self, info, id):
        return AdoptedModel.objects.get(pk=id)
    
    def resolve_charses(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], CharsModel)
        return CharsModel.objects.all()
    def resolve_chars(self, info, id):
        return CharsModel.objects.get(pk=id)
    
    def resolve_forAdoptions(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], ForAdoptionModel)
        return ForAdoptionModel.objects.all()
    def resolve_forAdoption(self, info, id):
        return ForAdoptionModel.objects.get(pk=id)
    
    def resolve_mediaes(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], MediaModel)
        return MediaModel.objects.all()
    def resolve_media(self, info, id):
        return MediaModel.objects.get(pk=id)
    
    def resolve_pets(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], PetModel)
        return PetModel.objects.all()
    def resolve_pet(self, info, id):
        return PetModel.objects.get(pk=id)
    
    def resolve_razas(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], RazaModel)
        return RazaModel.objects.all()
    def resolve_raza(self, info, id):
        return RazaModel.objects.get(pk=id)
    
    def resolve_users(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], UserModel)
        return UserModel.objects.all()
    def resolve_user(self, info, id):
        return UserModel.objects.get(pk=id)
    
    def resolve_files(self, info, **kwargs):
        if "query" in kwargs:
            return query(kwargs["query"], FileModel)
        return FileModel.objects.all()
    def resolve_file(self, info, id):
        return FileModel.objects.get(pk=id)
