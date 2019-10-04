"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import Media
from app.models import User
from app.models import File
from seed.schema.types import Media as MediaType

class SaveMediaMutation(graphene.Mutation):
    
    media = graphene.Field(MediaType)
    
    class Arguments:
        fileName = graphene.String(required=True)
        url = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        media = {}
        if "fileName" in kwargs: media["file_name"] = kwargs["fileName"]
        if "url" in kwargs: media["url"] = kwargs["url"]
        media = Media.objects.create(**media)
        media.save()
    
        return SaveMediaMutation(media=media)

class SetMediaMutation(graphene.Mutation):
    
    media = graphene.Field(MediaType)
    
    class Arguments:
        id = graphene.Int(required=True)
        fileName = graphene.String(required=False)
        url = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        media = Media.objects.get(pk=kwargs["id"])
        if "fileName" in kwargs: media.file_name = kwargs["fileName"]
        if "url" in kwargs: media.url = kwargs["url"]
        media.save()
    
        return SetMediaMutation(media=media)

class DeleteMediaMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        media = Media.objects.get(pk=kwargs["id"])
        media.delete()
        return DeleteMediaMutation(id=id)
