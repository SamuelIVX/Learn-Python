#-------------------------------------------------------------------------
#Ternary Operator:
#Without:
def is_adult(age):
  if age > 18:
    return True
  else:
    return False

#With:
def is_adult2(age):
  return True if age > 18 else False
#-------------------------------------------------------------------------