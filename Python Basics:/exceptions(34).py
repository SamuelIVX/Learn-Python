#-------------------------------------------------------------------------
#Exceptions:
#It's important to handle errors and python gives us exception handling:
#Wrap lines of code in a try block:
try: 
  #Some lines of code
except <ERROR1>: #checking for a specific error and you can handle it here
  #handler error <ERROR1>
except <ERROR2>: #if a different error occurs you can handle it here
  #handler error <ERROR2>
#if an error occurs, python will tell you and you can determine which kind of error occured using an except block

#You can also catch all exceptions. By using an except without an error type.
  try: 
  #Some lines of code
except <ERROR1>: #You actually have to put a SPECIFIC error in the "<ERROR1>" place. This is just an example!!!
  #handler error <ERROR1>
except <ERROR2>:
  #handler error <ERROR2>
  except:

#You can also put an "else" block at the end that will run if NO exceptions are found.
    try: 
  #Some lines of code
except <ERROR1>: #You actually have to put a SPECIFIC error in the "<ERROR1>" place. This is just an example!!!
  #handler error <ERROR1>
except <ERROR2>:
  #handler error <ERROR2>
else:

#Can also add a finally block. Anything inside the block will always run at the end whether or not there were execptions. Alwways going to run.

#Example:
result = 2 / 0
print(result) #0 division error

#With try block:
try:
  result = 2 / 0
except ZeroDivisionError:
  print("Cannot be divided by 0!")
finally:
  result = 1
  
print(result) #1

raise Execption("An Error") #You can also raise your own general exception using this syntax
#You can intercept it by:
try: 
  raise Execption("An Error")
except Exception as error:
  print(error)

#You can also define your own exception class extending from exception:
class DogNotFoundException(Exception):
  pass #Means we are nothing going to have any code in this definition block

try: 
  raise DogNotFoundException()
except DogNotFoundException:
  print("Dog Not found!")

#You can handle this execption and can also add something inside the exception. (Before the pass)
#-------------------------------------------------------------------------