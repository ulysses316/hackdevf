"""
__Seed builder__v1.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene

import seed.schema.types
import seed.mutations.adopted
import seed.mutations.chars
import seed.mutations.for_adoption
import seed.mutations.media
import seed.mutations.pet
import seed.mutations.raza
import seed.mutations.user

class _Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class _Mutation(graphene.ObjectType):
    
    saveAdopted = seed.mutations.adopted.SaveAdoptedMutation.Field()
    setAdopted = seed.mutations.adopted.SetAdoptedMutation.Field()
    deleteAdopted = seed.mutations.adopted.DeleteAdoptedMutation.Field()
    saveChars = seed.mutations.chars.SaveCharsMutation.Field()
    setChars = seed.mutations.chars.SetCharsMutation.Field()
    deleteChars = seed.mutations.chars.DeleteCharsMutation.Field()
    saveForAdoption = seed.mutations.for_adoption.SaveForAdoptionMutation.Field()
    setForAdoption = seed.mutations.for_adoption.SetForAdoptionMutation.Field()
    deleteForAdoption = seed.mutations.for_adoption.DeleteForAdoptionMutation.Field()
    saveMedia = seed.mutations.media.SaveMediaMutation.Field()
    setMedia = seed.mutations.media.SetMediaMutation.Field()
    deleteMedia = seed.mutations.media.DeleteMediaMutation.Field()
    savePet = seed.mutations.pet.SavePetMutation.Field()
    setPet = seed.mutations.pet.SetPetMutation.Field()
    deletePet = seed.mutations.pet.DeletePetMutation.Field()
    saveRaza = seed.mutations.raza.SaveRazaMutation.Field()
    setRaza = seed.mutations.raza.SetRazaMutation.Field()
    deleteRaza = seed.mutations.raza.DeleteRazaMutation.Field()
    saveUser = seed.mutations.user.SaveUserMutation.Field()
    setUser = seed.mutations.user.SetUserMutation.Field()
    deleteUser = seed.mutations.user.DeleteUserMutation.Field()


