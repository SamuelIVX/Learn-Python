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