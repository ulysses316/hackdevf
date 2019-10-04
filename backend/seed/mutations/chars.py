"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Chars
from app.models import Pet
from app.models import File
from seed.schema.types import Chars as CharsType

class SaveCharsMutation(graphene.Mutation):
    
    chars = graphene.Field(CharsType)
    
    class Arguments:
        size = graphene.Int(required=True)
        weight = graphene.Int(required=True)
        color = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        chars = {}
        if "size" in kwargs: chars["size"] = kwargs["size"]
        if "weight" in kwargs: chars["weight"] = kwargs["weight"]
        if "color" in kwargs: chars["color"] = kwargs["color"]
        chars = Chars.objects.create(**chars)
        chars.save()
    
        return SaveCharsMutation(chars=chars)

class SetCharsMutation(graphene.Mutation):
    
    chars = graphene.Field(CharsType)
    
    class Arguments:
        id = graphene.Int(required=True)
        size = graphene.Int(required=False)
        weight = graphene.Int(required=False)
        color = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        chars = Chars.objects.get(pk=kwargs["id"])
        if "size" in kwargs: chars.size = kwargs["size"]
        if "weight" in kwargs: chars.weight = kwargs["weight"]
        if "color" in kwargs: chars.color = kwargs["color"]
        chars.save()
    
        return SetCharsMutation(chars=chars)

class DeleteCharsMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        chars = Chars.objects.get(pk=kwargs["id"])
        chars.delete()
        return DeleteCharsMutation(id=id)
