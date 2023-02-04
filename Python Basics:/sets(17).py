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