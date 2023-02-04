#-------------------------------------------------------------------------
#Classes
#We can declare our own classes and instantiate objects. An object is an instance of a class and a class is a type of the object.
class Dog:
  def bark(self): #Self is an argument of the method that will point to the current object instance. It **MUST** be specfied when defining a method. So when you create a method inside a class, you always start with "self"
    print("woof!")
roger = Dog()
print(type(roger)) #will print out what class "roger" is in (AKA the Dog class).

class Dog:
  #This is a constructor. Used to initialize one more properties when we create a new OBJECT from that CLASS.
  def __init__(self, name, age): #Once again we add self. Now we have two new variables that we can pass in when we create a dog. It will be associated with that object.
    self.name = name
    self.age = age 
  def bark(self):
    print("woof")
roger = Dog("Roger", 8) #So now we can pass two arguments for the name and age
print(roger.name) #We can access the variables inside the constructor by using this syntax. This will print out Roger
print(roger.age) #This will print out 8
print(roger.bark()) #This will print out woof! It also says none since you don't need to wrap roger.bark() in print since it is already printing something else (print("woof!")). To fix this problem, you can RETURN woof to the function bark, or just not do the print (roger.bark()).

#One important feature of classes is INHERITANCE
class Animal: #Create a class that is generalizing what the other classes are about. E.g: Main class is Car. Subclass inheriting the car attributes is a Toyota.
  def walk(self):
    print("walking...")
    
class Dog(Animal): #Now the dog class will inherit from the animal class
  def __init__(self, name, age): 
    self.name = name
    self.age = age 
  def bark(self):
    print("woof")
roger = Dog("Roger", 8) 
print(roger.name) 
print(roger.age) 
roger.bark()
roger.walk() #As you cann see the Dog class does not have a walk method. But it is inheriting the walk method from the Animal class.
#-------------------------------------------------------------------------