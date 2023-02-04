#-------------------------------------------------------------------------
#Functions:
def hello(): #function name is hello
  print("Hello") #This is the function definition (what's inside a function)

#You have to call a function to execute it:
hello()
#The function name should be descriptive so anyone calling knows what it does

#Functions can take parameters (values accepted by the function inside the funciton definition):
def hello(name):
  print("Hello " + name)

#Enter the ARGUMENT (Are the values passed to the function)
hello("Samuel")

#You can also call a function with writing an argument making it optional:
def hello(name = "hello friend"):
  print("Hello " + name)
  
hello()

#Multiple Parameters:
def hello(name, age):
  print("Hello " + name + ", you are " + str(age) + " years old!")

hello("Sam", 17)

#Return Statements:
def hello(name):
  print("Hello " + name + "!")
  return
#When the return executes, the function ends.

#Can also return multiple values:
def hello(name):
  print("Hello " + name + "!")
  return name, "Sam", 8
  
print(hello("poop"))
#-------------------------------------------------------------------------