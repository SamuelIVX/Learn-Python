#-------------------------------------------------------------------------
#Modules
#A Python file is a module. You can import a module from other files. Promotes code reuse and simplicity.

#So I created a new file called dog.py and wrote a method called bark that when called, it will print out "woof!". In order to use that method, I imported dog (name of the file), and now I have access to the method
import dog
dog.bark()

#We can also use the "from import" syntax and call the function directly
from dog import bark
bark()

#If you want to get access the modules from a file that's INSIDE a folder you need to do something like this
from lib import dog
dog.bark()
#The folder is called lib and we want to import whats inside the dog file. There is an __init__.py file inside the folder since this tells Python that the folder contains MODULES.

#If you want to import a specific function from a file inside a folder, use something like this:
from lib.dog import bark
bark()

#Pre-Built Modules
#We can use Python's standard library to import a huge collection of utilities. Some examples are:

#math for math utilities
#re for regular expressions
#json to work with JSON
#datetime to work with dates
#sqlite3 to use SQlite
#os for Operating System Utilities
#random for random number generation
#statistics for statistics utilities
#requests to perform HTTP network requests
#http to create HTTP servers
#urllib to manage URLS

#You can import these modules that allow you to gain extra functionality.

#We will use the math one for an example:
import math

print(math.sqrt(4))
 #As mentioned before we can also do this:
from math import sqrt
print(sqrt(4))
#-------------------------------------------------------------------------