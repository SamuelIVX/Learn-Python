#-------------------------------------------------------------------------
#Decorators(Are a way to change, enhance or alter in any way how a function works. Decorators are defined with the "@" symbol, followed by the decorator name just before the function definition):
def logtime(func):
  def wrapper():
    print("before")
    val = func()
    print("after")
    return val
  return wrapper
  
@logtime #The function has the logtime decorator assigned. So whenever we call the hello function. The decorator will be called. A decorator is a function that takes in a function as a parameter and wraps the function in a inner function that performs the job it has to do and returns that inner function
def hello():
  print("hello")
hello()
#decorators are used when you wanna change the behavior a function without modifying the function itself.
#-------------------------------------------------------------------------
