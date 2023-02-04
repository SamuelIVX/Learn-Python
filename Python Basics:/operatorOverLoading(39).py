#-------------------------------------------------------------------------
#Operator Overloading:
#Advanced technique which we can use to make classes comparable and to make them work with python operators.

class Dog:
  #the dog class
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __gt__(self,other) #__gt__function is going to compare things to figure out what is greater than. Able to compare two dog objects
  return True if self.age > other.age else False

roger = Dog("Roger", 8)
syd = Dog("Syd", 7)
print(roger > syd) #This will print out True'
#can use operator overloading to add a custom way to compare these two objects based on the age property.

#Can create methods to go with different arithmetic operators:
# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator
#**Not limited to this methods**
#-------------------------------------------------------------------------