# Base models

## Table of content
-  [Adopted](#Adopted)
-  [Chars](#Chars)
-  [ForAdoption](#ForAdoption)
-  [Media](#Media)
-  [Pet](#Pet)
-  [Raza](#Raza)
-  [User](#User)

##  Adopted

-  Attributes:
   -  id: int
   -  users: user[]
   -  pets: pet[]

-  Reference: [Adopted](../seed/models/adopted.py)

##  Chars

-  Attributes:
   -  id: int
   -  size: int
   -  weight: int
   -  color: string
   -  pet: pet[]

-  Reference: [Chars](../seed/models/chars.py)

##  ForAdoption

-  Attributes:
   -  id: int
   -  users: user[]
   -  pets: pet[]

-  Reference: [ForAdoption](../seed/models/for_adoption.py)

##  Media

-  Attributes:
   -  id: int
   -  file_name: string
   -  url: string
   -  user: user[]

-  Reference: [Media](../seed/models/media.py)

##  Pet

-  Attributes:
   -  id: int
   -  name: string
   -  ster: boolean

-  Reference: [Pet](../seed/models/pet.py)

##  Raza

-  Attributes:
   -  id: int
   -  raza: string
   -  pet: pet[]

-  Reference: [Raza](../seed/models/raza.py)

##  User

-  Attributes:
   -  id: int
   -  username: string
   -  first_name: string
   -  last_name: string
   -  email: string
   -  is_active: boolean
   -  house_size: int
   -  pet_number: int
   -  city: string
   -  tel: int
   -  facebook: string

-  Reference: [User](../seed/models/user.py)

