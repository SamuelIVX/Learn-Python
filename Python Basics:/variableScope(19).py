#-------------------------------------------------------------------------
#Variable Scope:
age = 8
#This variable is declared outside of the function. This is visible and be used by any piece of code. This is called a GLOBAL variable.

def test():
  print(age)

print(age) #8
test() #8

def test():
  age = 8
  print(age)
#But now if it's inside the function, it is now a LOCAL variable, meaning it's only visible to the function.
#-------------------------------------------------------------------------