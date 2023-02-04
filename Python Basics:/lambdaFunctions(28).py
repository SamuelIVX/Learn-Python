#-------------------------------------------------------------------------
#Lambda Functions (Also called anonymous functions):
# the num after "lambda" is called the argument. The num after the colons is called the expression. The body must be a SINGLE expression and NOT a statement
lambda num : num * 2

#Lambda functions can accept more arguments and Lambda cannot be invoked directly but can be assigned to variables
multiply = lambda a,b : a * b
print(multiply(2,4)) #returns 8

#This can be used when combined with Python functionality. For example, math, filter, and reduce
#-------------------------------------------------------------------------