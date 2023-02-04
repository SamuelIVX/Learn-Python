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