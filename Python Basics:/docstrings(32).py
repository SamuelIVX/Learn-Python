#-------------------------------------------------------------------------
#Docstrings:
#reading and understanding code is very important, especially when you look back at old code work. So many people write comments just like this is a comment. But another way is to use Docstring.
def increment(n)
  """Increment a number""" #3 Quotations on either side and then type a description of whatever the code is.
return n + 1

#More Examples:
class Dog:
  """A class representing a Dog"""
  def __init__(self,name,age):
    """Initialize a new dog"""
    self.name = name
    self.age = age
  def bark(self):
    """Let the dog bark"""
    print("WOOF!")

#Common to add a docstring on the top of the file like:
"""

Write whatever this file does...

"""

#Python will process these docstrings and you can use the help global function to get the documentation of the class, method or function or a module
print(help(Dog))
#You will get the information abt the Dog class! This is why it's a good reason to use docstrings because there are specific standards and it's easier to get information.
#-------------------------------------------------------------------------