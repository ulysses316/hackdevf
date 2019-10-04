"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Raza
from app.models import Pet
from app.models import File
from seed.schema.types import Raza as RazaType

class SaveRazaMutation(graphene.Mutation):
    
    raza = graphene.Field(RazaType)
    
    class Arguments:
        raza = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        raza = {}
        if "raza" in kwargs: raza["raza"] = kwargs["raza"]
        raza = Raza.objects.create(**raza)
        raza.save()
    
        return SaveRazaMutation(raza=raza)

class SetRazaMutation(graphene.Mutation):
    
    raza = graphene.Field(RazaType)
    
    class Arguments:
        id = graphene.Int(required=True)
        raza = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        raza = Raza.objects.get(pk=kwargs["id"])
        if "raza" in kwargs: raza.raza = kwargs["raza"]
        raza.save()
    
        return SetRazaMutation(raza=raza)

class DeleteRazaMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        raza = Raza.objects.get(pk=kwargs["id"])
        raza.delete()
        return DeleteRazaMutation(id=id)
