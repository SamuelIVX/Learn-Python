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