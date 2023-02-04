#-------------------------------------------------------------------------
#Polymorphisim:
#Generalizes a functionality so it can work on different types. Important concept in Object Oriented Programming (OOP).
class Dog: 
  def eat(self):
    print("Eating dog food")
#Same method for both classes
class Cat:
  def eat(self):
    print("Eating cat food")

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()
#-------------------------------------------------------------------------