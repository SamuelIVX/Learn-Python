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