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