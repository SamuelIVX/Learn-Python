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