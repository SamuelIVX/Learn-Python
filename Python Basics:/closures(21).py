#-------------------------------------------------------------------------
#Closures
#If you return a nested function from a function, that nested function will have access to the variables defined in that function even thought the function is not active anymore.

def counter():
  count = 0
    
  def increment():
      nonlocal count 
      count += 1
      return count # We are returning count from this nested function
    
  return increment #and from the outer function we're returning the nested function

increment = counter() #Instead of calling the outer function directly, we are assigning it to this variable
print(increment()) #1
print(increment()) #2
print(increment()) #3
#Because we are calling the inner function, the local variable count will be reset to 0 everytime. It will keep track of the value.
#-------------------------------------------------------------------------