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