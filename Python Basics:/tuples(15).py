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