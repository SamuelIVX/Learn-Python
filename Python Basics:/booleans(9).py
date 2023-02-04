#-------------------------------------------------------------------------
#Booleans:
done = True
if done:
  print("yes")
else:
  print("no")
#Every int returns TRUE besides 0
#Empty Strings,Lists, Dictionaries, Tuples, return false (vice versa)

#The any operator is useful with booleans:
book_1_read = True
book_2_read = False
read_any_book = any([book_1_read, book_2_read])
#Will return TRUE since it checks if ANY of them are TRUE. Then it sets read_any_book to TRUE

#The all operator is also useful:
ingredients_purchased = True
meal_cooked = False

ready_to_serve = all([ingredients_purchased, meal_cooked])
#Checks if ALL values are TRUE. In this case it returns FALSE
#-------------------------------------------------------------------------