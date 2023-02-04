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