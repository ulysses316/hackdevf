"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Pet
from app.models import File
from seed.schema.types import Pet as PetType

class SavePetMutation(graphene.Mutation):
    
    pet = graphene.Field(PetType)
    
    class Arguments:
        name = graphene.String(required=True)
        ster = graphene.Boolean(required=True)

    def mutate(self, info, **kwargs):

        pet = {}
        if "name" in kwargs: pet["name"] = kwargs["name"]
        if "ster" in kwargs: pet["ster"] = kwargs["ster"]
        pet = Pet.objects.create(**pet)
        pet.save()
    
        return SavePetMutation(pet=pet)

class SetPetMutation(graphene.Mutation):
    
    pet = graphene.Field(PetType)
    
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)
        ster = graphene.Boolean(required=False)

    def mutate(self, info, **kwargs):

        pet = Pet.objects.get(pk=kwargs["id"])
        if "name" in kwargs: pet.name = kwargs["name"]
        if "ster" in kwargs: pet.ster = kwargs["ster"]
        pet.save()
    
        return SetPetMutation(pet=pet)

class DeletePetMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        pet = Pet.objects.get(pk=kwargs["id"])
        pet.delete()
        return DeletePetMutation(id=id)
