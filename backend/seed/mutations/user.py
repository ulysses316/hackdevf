"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from graphene_django import DjangoObjectType
from app.models import User
from app.models import File
from seed.schema.types import User as UserType

class SaveUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        username = graphene.String(required=True)
        firstName = graphene.String(required=True)
        lastName = graphene.String(required=True)
        email = graphene.String(required=True)
        isActive = graphene.Boolean(required=True)
        password = graphene.String(required=True)
        houseSize = graphene.Int(required=True)
        petNumber = graphene.Int(required=True)
        city = graphene.String(required=True)
        tel = graphene.Int(required=True)
        facebook = graphene.String(required=True)

    def mutate(self, info, **kwargs):

        user = {}
        if "userName" in kwargs: user["user_name"] = kwargs["userName"]
        if "firstName" in kwargs: user["first_name"] = kwargs["firstName"]
        if "lastName" in kwargs: user["last_name"] = kwargs["lastName"]
        if "email" in kwargs: user["email"] = kwargs["email"]
        if "isActive" in kwargs: user["is_active"] = kwargs["isActive"]
        if "houseSize" in kwargs: user["house_size"] = kwargs["houseSize"]
        if "petNumber" in kwargs: user["pet_number"] = kwargs["petNumber"]
        if "city" in kwargs: user["city"] = kwargs["city"]
        if "tel" in kwargs: user["tel"] = kwargs["tel"]
        if "facebook" in kwargs: user["facebook"] = kwargs["facebook"]
        user = User.objects.create(**user)
        if "password" in kwargs: user.setPassword(kwargs["password"])
        user.save()
    
        return SaveUserMutation(user=user)

class SetUserMutation(graphene.Mutation):
    
    user = graphene.Field(UserType)
    
    class Arguments:
        id = graphene.Int(required=True)
        username = graphene.String(required=False)
        firstName = graphene.String(required=False)
        lastName = graphene.String(required=False)
        email = graphene.String(required=False)
        isActive = graphene.Boolean(required=False)
        password = graphene.String(required=False)
        houseSize = graphene.Int(required=False)
        petNumber = graphene.Int(required=False)
        city = graphene.String(required=False)
        tel = graphene.Int(required=False)
        facebook = graphene.String(required=False)

    def mutate(self, info, **kwargs):

        user = User.objects.get(pk=kwargs["id"])
        if "userName" in kwargs: user.user_name = kwargs["userName"]
        if "firstName" in kwargs: user.first_name = kwargs["firstName"]
        if "lastName" in kwargs: user.last_name = kwargs["lastName"]
        if "email" in kwargs: user.email = kwargs["email"]
        if "isActive" in kwargs: user.is_active = kwargs["isActive"]
        if "password" in kwargs: user.setPassword(kwargs["password"])
        if "houseSize" in kwargs: user.house_size = kwargs["houseSize"]
        if "petNumber" in kwargs: user.pet_number = kwargs["petNumber"]
        if "city" in kwargs: user.city = kwargs["city"]
        if "tel" in kwargs: user.tel = kwargs["tel"]
        if "facebook" in kwargs: user.facebook = kwargs["facebook"]
        user.save()
    
        return SetUserMutation(user=user)

class DeleteUserMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        id = kwargs["id"]
        user = User.objects.get(pk=kwargs["id"])
        user.delete()
        return DeleteUserMutation(id=id)