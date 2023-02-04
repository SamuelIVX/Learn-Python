#-------------------------------------------------------------------------
#Recursion:
#Where a function calls itself. One of the most powerful things to do in coding if you understand it.
#Common way to understand recursion is by using the factorial calculation:

#Not Python code just showing what a factorial is.
3! = 3 * 2 * 1 = 6 #So 3! (factorial means)
4! = 4 * 3 * 2 * 1 = 24
5! = 5 * 4 * 3 * 2 * 1 = 120

#So with recursion we can makie it so we can get any factorial for a number:
def factorial(n):
  if n == 1: return 1 #Always has a base case (when we are going to leave the recurvise fucntion)
  return n * factorial(n-1) #recursive (where we call the function)
print(factorial(3))
print(factorial(4))
print(factorial(5))
#-------------------------------------------------------------------------