#-------------------------------------------------------------------------
#Enums(Readable names that are bound to a constant value):
#Will have to import
from enum import Enum

class State(Enum):
  INACTIVE = 0
  ACTIVE = 1
  
print(State(1))
print(State.ACTIVE.value)
print(State["ACTIVE"])
print(State["ACTIVE"].value)
#Basically the only way to create constants in Python

#Listing the values:
print(list(State))

#Can also count them:
print(len(State))
#-------------------------------------------------------------------------