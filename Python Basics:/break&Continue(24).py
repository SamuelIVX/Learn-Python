#-------------------------------------------------------------------------
#Break and Continue
#Both while loops and for loops can be interupted inside the block using either break or continue
#Continue: stops the current iteration and executes the next one
items = [1,2,3,4]
for item in items:
  if item == 2:
    continue
    print(item)
#It will not print out the item, "2", since it skipped that iteration and went to the next one.
  
#Break: stops the loop all together and goes on to the next instruction and executes that one.
items = [1,2,3,4]
for item in items:
  if item == 2:
    break
    print(item)
# It wil just print one since it broke out of the loop entirely when it reached "break".
#-------------------------------------------------------------------------