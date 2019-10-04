"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Adopted
from app.models import User
from app.models import Pet
from app.models import File
from seed.schema.types import Adopted as AdoptedType

class SaveAdoptedMutation(graphene.Mutation):
    
    adopted = graphene.Field(AdoptedType)
    
    class Arguments:
        users = graphene.List(graphene.Int)
        pets = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):

        adopted = {}
        adopted = Adopted.objects.create(**adopted)
        if "users" in kwargs:
            adopted.user = [] 
            for id in kwargs["users"]:
                users = User.objects.get(pk = id)
                adopted.users.add(users)
        if "pets" in kwargs:
            adopted.pet = [] 
            for id in kwargs["pets"]:
                pets = Pet.objects.get(pk = id)
                adopted.pets.add(pets)
        adopted.save()
    
        return SaveAdoptedMutation(adopted=adopted)

class SetAdoptedMutation(graphene.Mutation):
    
    adopted = graphene.Field(AdoptedType)
    
    class Arguments:
        id = graphene.Int(required=True)
        users = graphene.List(graphene.Int)
        pets = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):

        adopted = Adopted.objects.get(pk=kwargs["id"])
        if "users" in kwargs:
            adopted.user = [] 
            for id in kwargs["users"]:
                users = User.objects.get(pk = id)
                adopted.users.add(users)
        if "pets" in kwargs:
            adopted.pet = [] 
            for id in kwargs["pets"]:
                pets = Pet.objects.get(pk = id)
                adopted.pets.add(pets)
        adopted.save()
    
        return SetAdoptedMutation(adopted=adopted)

class DeleteAdoptedMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        adopted = Adopted.objects.get(pk=kwargs["id"])
        adopted.delete()
        return DeleteAdoptedMutation(id=id)
