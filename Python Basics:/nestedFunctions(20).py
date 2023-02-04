#-------------------------------------------------------------------------
#Nested Fuunctions
def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)
talk("I am going to buy the milk")
#Will split each word. Create a list for every word individually.

def count():
  count = 0
  def increment():
      nonlocal count #Nonlocal allows us to access the count variable that was declared outside this function.
      count += 1
      print(count)
  increment()
count()
#-------------------------------------------------------------------------