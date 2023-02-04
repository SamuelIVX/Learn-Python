#-------------------------------------------------------------------------
#Arguments from Command Line:
#You can easily run a program by hitting the "run" button in different IDE's. But you can also run programs in command lines. (AKA the "Shell" tab in Replit)
print("hello")

#In order to run a prorgram. Do this:
#python main.py

#Where obviously we are using python and calling the file we want to run.

#But we can also pass in arguments in the comamand line. A basic way to handle arguments, is to use the "sys module" from the standard library. **USUALLY YOU HAVE IMPORT STATEMENTS ON THE FIRST LINES AND A COMMENT FOR A REMINDER**
import sys

print(sys.argv)

#So now when you run the file from the comman line, you can do something like this:
#python main.py Sam 23

#This will print out the list of the arguments

#So then you can do something like this:
name = sys.argv[1]
print("Hello " + name)

#So after calling it again, and putting in an argument like Sam, it will pass in that argument and assign it into the variable "name". Yet this module makes you do more work since you need to validate the user what kind of arguments are accepted and not
#Python provides another package in the standard library called argparse.
import argparse

parser = argparse.ArgumentParser( #calling it
  description = "This program prints the name of my cats" #passing in the description of the program
)
#Proceed to add arguments you want to accept:
parser.add_argument("-c", "--color", metavar = "color", required = True, help = "the color to search for")
#So when you run the file, you can either pass in the argument "-c" or "--color". Then insert a color which will be passed on to the "metavar" variable and calling the color you inserted, "color". 
args = parser.parse_args()
print(args.color)

#If you don't specify an argument then it will serve as an error telling you what is required.

#You can also add choices after the required section.
parser.add_argument("-c", "--color", metavar = "color", required = True, choices = {"red", "yellow"}, help = "the color to search for")
#Now it can only accept two options. Red or yellow.
#If you call it again and insert a color other than the colors it can only accept, it will tell you that your input was an "invalid choice", and gives you the list of choices.
args = parser.parse_args()
print(args.color)

#This makes it easier to communicate information to the user on what we are trying to get
#-------------------------------------------------------------------------
