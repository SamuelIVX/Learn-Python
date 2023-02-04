#You can use the ** command + f ** button to find what you are looking for but I also broke down each individual fundamental inside their own files**

# INDENTATION matters in Python!

#-------------------------------------------------------------------------
#You can put both of these STATEMENTS in seperate lines but by typing a semicolon, this also works.
name = "sam"; print(name)

#We can also check DATA TYPES. For example:
print(type(name)) #This prints out the DATA TYPE of the variable                     name

#We can also compare it. For example:
print(type(name) == str) #This evalutes to TRUE and vice versa if                            it isn't a string

#We can also use isinstance. This checks if name is an INSTANCE of a string. For example:
print(isinstance(name, str)) #We pass two things. We pass the                                   variable and the data type 
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#DATA TYPES:
#complex = complex numbers
#bool = booleans (Returns true or false)
#list(or arrays) = lists
#tuple = tuples
#range = ranges
#dict = dictionaries
#set = sets
#str = words and characters surrounded by quotation marks
#int = whole numbers
#float = decimals
#Exploring these soon!

#We can assign DATA TYPES to VARIABLES:
price = float(2.9)
print(isinstance(price, float))

#We can also CONVERT from one data type to another:
age = int("20")
print(isinstance(age, int))

#We can also pass in a variable:
number = "54"        
newAge = int(number)
print(isinstance(newAge, int))
#So the variable number was originally a string but we converted it into an integer^. This is called CASTING.abs

#Errors can occur using this method. For example:
  #newNumber = "test"
  #testingNum = int(newNumber)
  #print(isinstance(testingNum, int))
#An error occurs here since test can't be converted into a number, obviously since it's a word.
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#ARITHMETIC OPERATORS:
# 1 + 1 = 2
# 2 - 1 = 1
# 2 * 2 = 4
# 4 / 2 = 2
# 4 % 3 = 1 (Returns the remainder! % = Modulus or Mod for short)
# 4 ** 2 = 16 (4 to the power of 2)
# 4 // 2 = 2 (Floor Division. This ROUNDS DOWN to the nearest WHOLE number)

#Comparison Operators:
# a == b (Are they equal?)
# a != b (A does not equal B)
# a < b (Less then)
# a <= b (less than or equal to)

#Boolean Operators:
#not condition1 (False)
#condition1 and condition2 (False, Both have to be true)
#condition1 or condition2 (True, only one needs to be true)

#RETURNS THE FIRST OPERAND THAT IS NOT A FALSEY VALUE:
#print(0 or 1) ##1
#print(False or "hey") ##hey
#print("hi" or "hey") ##hi
#print([] or false) ##False
#print(False or []) ##[] (This is considered a falsey value)

# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# performs a binary NOT operation
# << shift left operation
# >> shift right operation
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#IS and IN Operators:
#Is (Identity Operator): Used to compare two objects and returns true if both are the same objects
#In (Membership Operator): tells if a value is in a list or in another sequence
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Ternary Operator:
#Without:
def is_adult(age):
  if age > 18:
    return True
  else:
    return False

#With:
def is_adult2(age):
  return True if age > 18 else False
#-------------------------------------------------------------------------
  
#-------------------------------------------------------------------------
#Multi-Line String:
print("""Sam is

my

name
""")
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#String Methods:
print("Sam".upper()) ## uppercase
print("Sam".isupper()) #checks if all letters are uppercasedcased
print("Sam".lower()) ## lowercase
print("Sam".islower()) #checks if all letters are lowercased
print("sam hernandez".title()) ## makes each first letter of a word capatilized

#startswith(): to check if the string starts with a specfic substring
#endswith(): to check if the string ends with a specfic substring
#replace():to replace a part of a string
#split(): to split a string on a specific character
#strip(): to trim the whitespace from a string
#join(): to append new letters to a string
#find(): to find the position of a substring
#isalpha(): to check if a string contains only characters and is not empty
#isalnum(): to check if a string contains characters or digitsand is not empty
#isdecimal(): to check if a string contains digits and is not empty

#name = "Samuel"
#print(len(name)): returns the length
#print("am" in name): returns True if the substring is in the String else False

#Escaping Characters:
#\" (Adds a quote in a String)
#\\ (Adds a slash in a String)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#String Characters and Slicing:
#INDEX STARTS AT 0 NOT 1!
name = "Hernandez"
print(name[0]) #Starts at index 0
print(name[-1]) #Starts at the last letter
print(name[1:4]) #Starts at index 1 and ends at index 4. Retuns the letters between them
print(name[:5]) #Returns everything up to index 5
print(name[5:]) #Starts at the ends and returns everything up to -5
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Booleans:
done = True
if done:
  print("yes")
else:
  print("no")
#Every int returns TRUE besides 0
#Empty Strings,Lists, Dictionaries, Tuples, return false (vice versa)

#The any operator is useful with booleans:
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
#Will return TRUE since it checks if ANY of them are TRUE. Then it sets read_any_book to TRUE
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#The all operator is also useful:
ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
#Checks if ALL values are TRUE. In this case it returns FALSE
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Number Data Types:
num1 = 2+3j #j is the imaginary #
#OR you can use the complex constructor
num2 = complex(2,3) #where the first slot is the REAL int and the second slot is the IMAGINARY #

#Once you have a complex #, you can get the real or imaginary part of it:
print(num2.real, num2.imag)
#Will be returned as floats
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Built-in Functions:
print(abs(-5.5)) #Returns the absolute value of a #
print(round(5.5)) #Rounds to the nearest integer
print(round(5.5,1)) #Rounds to the first decimal point (Tenths value)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Enums(Readable names that are bound to a constant value):
#Will have to import
from enum import Enum

class State(Enum):
  INACTIVE = 0
  ACTIVE = 1
  
print(State(1))
print(State.ACTIVE.value)
print(State["ACTIVE"])
print(State["ACTIVE"].value)
#Basically the only way to create constants in Python

#Listing the values:
print(list(State))

#Can also count them:
print(len(State))
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#USER INPUT:
#1st Way:
print("What is your age?")
age = input()
print("Your age is: " + age)
#2nd Way:
age = input("What is your age?")
print("Your age is: " + age)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Lists:
dogs = ["Roger", 1, "Syd", True, "Poop", 7] #Can hold multiple values and can hold multiple DIFFERENT data types (Int, Bool, Strings...)
dogs2 = [] #Can create an empty list

#Checks if an item is in a list:
print("Roger" in dogs)

#Returns the item by the index:
print(dogs[0])

#Can also use negatives:
print(dogs[-1])

#Can update the list by changing an item by an index:
dogs[2] = "Sam"

#As used before, you can use this:
print(dogs[2:4])

print(dogs[2:]) #Starts at index 2 and goes through the end of the list

#Good way to slice the list:
print(dogs[:3])

#Can add an item to a list:
dogs.append("Judah")

#Can also use length method:
print(len(dogs))

#Can add a list to a list using the extend method:
dogs.extend(["New List", 5]) 
#OR can use the += operator which does the same thing:
dogs += ["Using Extend", 8]

#Can remove items from a list using the remove method:
dogs.remove("Poop")

#Pop method (Returns and removes the last item in a list)
print(dogs.pop())

#How to add an item into a specfic index (Insert Method):
items = ["Wut", "Yeah", "woah"]
items.insert(2, "Test") #First Slot = Specific Index , Second Slot = What you want to insert
print(items)

#How to insert multiple items at a specific index:
items[1:1] = ["Test1", "Test2"]
print(items)

#How to sort a list (THE LIST HAS TO BE ONE SPECIFC DATA TYPE):
items2 = ["Bob", "Pre", "Roger", "Juan"]
items2.sort()
#Returns in alphabetical order
#If it's a list of ints or doubles, it returns them in numerical order

#Yet if you enter a lower case word into a list, the sort method will first sort the uppercase words THEN the lowercase ones:
items3 = ["Bob", "Pre", "Roger", "Juan", "sam"]
items3.sort()
#You can fix this by doing:
items3.sort(key=str.lower)

#You can also have a copy of your list by doing:
itemscopy = items3[:] #Does not have to be called itemscopy
print(itemscopy)

#How to print the original list AND the modified list. That way you don't modify the ORIGINAL list
sorted(items3, key=str.lower)
print(items3)

#Can see all the items in a list:
print(dogs)
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Tuples (Allow to create immutable groups of objects meaning you can't MODIFY(change) it):
names = ("Roger", "Syd", "Hernandez")
names[0] #Returns the item with the index 0
names.index("Roger") #Returns the index by the item
names[-1] #Can also use negatives
len(names) #Can also use the length method
print("Roger" in names) #Returns true since that item is in names
names[0:2] #Starts at index 0 and ends at index 2
print(sorted(names)) #Won't change the list into alphabetical order since it is IMMUTABLE

#Can create new Tuples by EXISTING Tuples:
newTuple = names + ("Tina", "Quincy")
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Dictionaries (Allows to create key value pairs):
dog = {"name": "Roger", "age": 8} #{Key: Value} (The key can be a String, # or a Tuple. The value can be anything)
print(dog["name"]) #Prints Roger

#How to change the value by using a key:
dog["name"] = "Syd"
print(dog)

#How to get a specifc element:
print(dog.get("name")) #Returns Roger

#Using the Pop Method (Retrieving the value of the key and delete the item from the dictionary):
print(dog.pop("name"))
print(dog)
#This will return the value corresponding to the key and delete it

#How to retrieve and remove the last key value pair inserted in the dictionary:
print(dog.popitem())
print(dog)

#Can also check if a key is contained in a dictionary:
print("color" in dog)

#How to return all the keys in a dictionary:
print(dog.keys())
#OR how to return the actual list part (preferred):
print(list(dog.keys()))

#Can also do the same thing with values:
print(dog.values())
print(list(dog.values()))

#Returning all the items in a dictionary and converting it into a list:
print(list(dog.items()))

#Length Function:
print(len(dog))

#Can also add a new key value pair into a dictionary:
dog["favorite food"] = "meat"
print(dog)

#Can also delete a key value pair:
del dog["name"]

#How to make a copy of a dictionary:
dogCopy = dog.copy() #doesn't have to be called dogCopy
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Sets(Work like tuples but they are not ordered and are immutable):
set1 = {"Roger", "Syd"}
set2 = {"Roger"}

#Can intersect two sets:
intersect = set1 & set2 
print(intersect) #Returns what word is in both sets

#Can also create a union of two sets
set3 = {"Richard", "Syd"}
set4 = {"Luna"}
mod = set3 | set4
print(mod) #Returns each iteam in both sets

#Can also get the differences between two sets:
set5 = {"Luna", "Syd"}
set6 = {"Luna"}
mod = set5 - set6 #returns what they don't have in common

#Can check if a set is a superset of another or a subset:
set7 = {"Luna", "Syd"}
set8 = {"Luna"}
mod = set5 > set6 #superset
mod = set5 < set6 #subset
print(mod)

#Can also use length:
print(len(mod))

#Can convert a set to a list:
print(list(set1))

#Can use the in method as well
#A SET CANNOT HAVE TWO OF THE SAME ITEM MAKING IT USEFUL.
#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------
#Variable Scope:
age = 8
#This variable is declared outside of the function. This is visible and be used by any piece of code. This is called a GLOBAL variable.

def test():
  print(age)

print(age) #8
test() #8

def test():
  age = 8
  print(age)
#But now if it's inside the function, it is now a LOCAL variable, meaning it's only visible to the function.
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Nested Fuunctions
def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)
talk("I am going to buy the milk")
#Will split each word. Create a list for every word individually.

def count():
  count = 0
  def increment():
      nonlocal count #Nonlocal allows us to access the count variable that was declared outside this function.
      count += 1
      print(count)
  increment()
count()
#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------
#Objects
#Everything in Python is an object. Objects have attributes and methods. They can be accessed using the "." syntax. #E.g:
age = 8

print(age.real)
print(age.imag)
print(age.bit_length()) #Returns the necessary amount of bits to represent this # in binary notation.

items = [1,2]

items.append(3)
items.pop()
print(id(items)) #Returns the location of items in the memory
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Loops
#There are two kinds of loops in Python: While loops and For Loops
condition = True
while condition == True:
  print("The condition is True")
#The will while loop will repeat the block until the condition is evaluated as false. This is an infinite loop.

while condition == True:
  print("The condition is True")
#Now this loop ends.

count = 0
while count < 10: #Count should be less than 10 meaning this loop will loop 9 times
  print("The condition is True")
  count += 1

  print("After the loop")

#For Loop
items = [1,2,3,4]
for item in items:
  print(item)
#Self-explanatory. It will iterate through the items lists and print each value.
  
#Using the range function, you can iterate through a list a specifc amount of times.
for item in range(15):#Basically returns a list.
  print(item)
#Will print 0 - 14

#This will return the index for each item. (Index, item)
items = [1,2,3,4]
for index, item in enumerate(items):
  print(index, item)
#Can do this for Strings
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Break and Continue
#Both while loops and for loops can be interupted inside the block using either break or continue
#Continue: stops the current iteration and executes the next one
items = [1,2,3,4]
for item in items:
  if item == 2:
    continue
    print(item)
#It will not print out the item, "2", since it skipped that iteration and went to the next one.
  
#Break: stops the loop all together and goes on to the next instruction and executes that one.
items = [1,2,3,4]
for item in items:
  if item == 2:
    break
    print(item)
# It wil just print one since it broke out of the loop entirely when it reached "break".
#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------
#Arguments from Command Line:
#You can easily run a program by hitting the "run" button in different IDE's. But you can also run programs in command lines. (AKA the "Shell" tab in Replit)
print("hello")

#In order to run a prorgram. Do this:
#python main.py

#Where obviously we are using python and calling the file we want to run.

#But we can also pass in arguments in the comamand line. A basic way to handle arguments, is to use the "sys module" from the standard library. **USUALLY YOU HAVE IMPORT STATEMENTS ON THE FIRST LINES AND A COMMENT FOR A REMINDER**
import sys

print(sys.argv)

#So now when you run the file from the comman line, you can do something like this:
#python main.py Sam 23

#This will print out the list of the arguments

#So then you can do something like this:
name = sys.argv[1]
print("Hello " + name)

#So after calling it again, and putting in an argument like Sam, it will pass in that argument and assign it into the variable "name". Yet this module makes you do more work since you need to validate the user what kind of arguments are accepted and not
#Python provides another package in the standard library called argparse.
import argparse

parser = argparse.ArgumentParser( #calling it
  description = "This program prints the name of my cats" #passing in the description of the program
)
#Proceed to add arguments you want to accept:
parser.add_argument("-c", "--color", metavar = "color", required = True, help = "the color to search for")
#So when you run the file, you can either pass in the argument "-c" or "--color". Then insert a color which will be passed on to the "metavar" variable and calling the color you inserted, "color". 
args = parser.parse_args()
print(args.color)

#If you don't specify an argument then it will serve as an error telling you what is required.

#You can also add choices after the required section.
parser.add_argument("-c", "--color", metavar = "color", required = True, choices = {"red", "yellow"}, help = "the color to search for")
#Now it can only accept two options. Red or yellow.
#If you call it again and insert a color other than the colors it can only accept, it will tell you that your input was an "invalid choice", and gives you the list of choices.
args = parser.parse_args()
print(args.color)

#This makes it easier to communicate information to the user on what we are trying to get
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Lambda Functions (Also called anonymous functions):
# the num after "lambda" is called the argument. The num after the colons is called the expression. The body must be a SINGLE expression and NOT a statement
lambda num : num * 2

#Lambda functions can accept more arguments and Lambda cannot be invoked directly but can be assigned to variables
multiply = lambda a,b : a * b
print(multiply(2,4)) #returns 8

#This can be used when combined with Python functionality. For example, math, filter, and reduce
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Map,Filter,Reduce:
#Python provides 3 useful functions that can be used to work with collections:
#Since they are functions, they have "()" at the end.

#Map is used to run a function upon each item in an iterable like a list

numbers = [1,2,3]
def double(a):
  return a * 2

#We are mapping through each item in the list by running the functon and running the list. Then we are getting a new list
result = map(double,numbers)
print(list(result)) #If you just print result, you'll get the map object. So pass it into a list function.

#When the function is a one-liner, it's common to use lambda:
numbers = [1,2,3]
double = lambda a : a * 2 #Does the same thing but simplified
result = map(double,numbers)
print(list(result))

#But you can simplify it more by doing:
numbers = [1,2,3]
result = map(lambda a : a * 2 ,numbers) #Now we are mapping over the lambda function
print(list(result)) #Still prints out the same thing but way more simplify

#Filter (Takes in an iterable and returns a filtered object which is another iterable but without some of the other items.):
numbers = [1,2,3,4,5,6]
def isEven(n):
  return n % 2 == 0 #This will return true if the item is divisible by 2
result = filter(isEven,numbers) #Any even number will be added to result and any odd number will not
print(list(result))

#As mentioned before, we can use a lambda function:
numbers = [1,2,3,4,5,6]
result = filter(lambda n : n % 2 == 0 ,numbers) #Does the same thing
print(list(result))

#Reduce (Used to calculate a value out of a sequence like a list):
#This is the long way of doing it without reduce:
expenses = [
  ("Dinner", 80)
  ("Car Repair", 120)
]

sum = 0
for expense in expenses:
  sum += expense[1] #So bascially we are taking in the 1ST INDEX and adding it to the sum variable. (Remember that lists start at 0 but we are adding the items that start at 1 meaning both 80 and 120)
print(sum) #This returns 200

#Quicker way with reduce:
#Reduce is different than both map and filter since you have to import it
from functools import reduce
expenses = [
  ("Dinner", 80)
  ("Car Repair", 120)
]
sum = reduce(lambda a, b : a[1] + b[1], expenses) #Expenses is the iterable and lambda has two take in two arguments. The first argument (a), is the accumulative value and the second argument (b) is the updated value from the iterable. We are bascially adding every item together and reduce the numbers in the 1st index down to 1 value.
print(sum) #Still returns 200
#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------
#With:
#Very helpful to simplify working with exception handling, for example using it with files:
#Without with:
filename = "/Users/sam/test.text"

try:
  file = open(filename, "r")
  content = file.read()
  print(content)
finally:
  file.close()

#So we opened the file, read the content, printed the content and closed the file

#Now using with:
with open(filename, "r") as file:
  content = file.read()
  print(content)
#Now it will automatically close the file at the end meaning we have built in implicit exception handling.
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#Third-Party Packages:
#How to install third-party packages such as pip:
#Individuals and companies create packages and make them available as open source software for the entire community. Over 270,000 packages freely available. Some devices already have pip installed. Replit for example already has it.abs

#How to install a package:
#1: Go to shell (If using a different IDE, go to terminal)
#2: pip install <enter package name>

#One popular package is: requests
#So "pip install requests"
#After it is done downloading, it will be available for all python scripts since packages are installed globally. 

#You can also upgrade a package to it's latest version:
# pip install -U <package name you want to upgrade>
# pip install -U requests

#Can also specify a certain version of a package AND uninstall a package
# pip uninstall requests

# pip show <enterpackagename> This shows information about the package
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
#List Compressions:
#Is a way to create lists in a very concise way.

numbers = [1,2,3,4,5]
#Can compress a new list using the numbers list but by the power of 2:
numbers_power_2 = [n**2 for n in numbers] #list compressions syntax
print(numbers_power_2)

#List compression is sometimes preferred over for loops since it is more readable

#This is how you do it with a loop:
numbers_power_2 = []
for n in numbers:
  numbers_power_2.append[n**2]

#Can also do the same thing with map as well:
numbers_power_2 = list(map(lambda n: n**2, numbers))
#-------------------------------------------------------------------------

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

#-------------------------------------------------------------------------
#Operator Overloading:
#Advanced technique which we can use to make classes comparable and to make them work with python operators.

class Dog:
  #the dog class
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def __gt__(self,other) #__gt__function is going to compare things to figure out what is greater than. Able to compare two dog objects
  return True if self.age > other.age else False

roger = Dog("Roger", 8)
syd = Dog("Syd", 7)
print(roger > syd) #This will print out True'
#can use operator overloading to add a custom way to compare these two objects based on the age property.

#Can create methods to go with different arithmetic operators:
# __add__() respond to the + operator
# __sub__() respond to the - operator
# __mul__() respond to the * operator
# __truediv__() respond to the / operator
# __floordiv__() respond to the // operator
# __mod__() respond to the % operator
# __pow__() respond to the ** operator
# __rshift__() respond to the >> operator
# __lshift__() respond to the << operator
# __and__() respond to the & operator
# __or__() respond to the | operator
# __xor__() respond to the ^ operator
#**Not limited to this methods**
#-------------------------------------------------------------------------