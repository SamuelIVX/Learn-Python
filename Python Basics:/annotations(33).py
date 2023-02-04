#-------------------------------------------------------------------------
#Annotations:
#Python is dynamically typed. So we don't have to define what type a function or method is unlike for example Java. But using annotations gives us the option to do that. 

#Without annotations
def increment(n):
  return n +1

#With annotations:
def increment(n: int) -> int: #So now we are specifying that this function only recieves and returns integers
  return n +1

#Can do this with variables:
#No annotation:
 count = 0
#With annotation:
count: int = 0
#Python will ignore this annotations like comments.

#A seperate tool called "mypy" can be run be standalone or integrated by IDE"s to automatically catch spelling erros, STATICALLY whille you are coding. It will also help you catch type mismatch bugs before even running code. Good help when your software becomes large and you want to refractor your code.
#-------------------------------------------------------------------------