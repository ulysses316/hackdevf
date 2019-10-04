"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import ForAdoption
from app.models import User
from app.models import Pet
from app.models import File
from seed.schema.types import ForAdoption as ForAdoptionType

class SaveForAdoptionMutation(graphene.Mutation):
    
    forAdoption = graphene.Field(ForAdoptionType)
    
    class Arguments:
        users = graphene.List(graphene.Int)
        pets = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):

        for_adoption = {}
        for_adoption = ForAdoption.objects.create(**for_adoption)
        if "users" in kwargs:
            for_adoption.user = [] 
            for id in kwargs["users"]:
                users = User.objects.get(pk = id)
                for_adoption.users.add(users)
        if "pets" in kwargs:
            for_adoption.pet = [] 
            for id in kwargs["pets"]:
                pets = Pet.objects.get(pk = id)
                for_adoption.pets.add(pets)
        for_adoption.save()
    
        return SaveForAdoptionMutation(forAdoption=for_adoption)

class SetForAdoptionMutation(graphene.Mutation):
    
    forAdoption = graphene.Field(ForAdoptionType)
    
    class Arguments:
        id = graphene.Int(required=True)
        users = graphene.List(graphene.Int)
        pets = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):

        for_adoption = ForAdoption.objects.get(pk=kwargs["id"])
        if "users" in kwargs:
            for_adoption.user = [] 
            for id in kwargs["users"]:
                users = User.objects.get(pk = id)
                for_adoption.users.add(users)
        if "pets" in kwargs:
            for_adoption.pet = [] 
            for id in kwargs["pets"]:
                pets = Pet.objects.get(pk = id)
                for_adoption.pets.add(pets)
        for_adoption.save()
    
        return SetForAdoptionMutation(forAdoption=for_adoption)

class DeleteForAdoptionMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        for_adoption = ForAdoption.objects.get(pk=kwargs["id"])
        for_adoption.delete()
        return DeleteForAdoptionMutation(id=id)
