# if ... elif ... else statements are used for program flow
# There can be zero or more elif parts, and the else part is optional. 
# The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation.
from statistics import mean

passcode = int(input("Enter password \n"))

if passcode == 1234:
    print("Logged in successfully")
else:
    print("Wrong password!")

# NB: The elif keyword is Python's way of saying "if the previous conditions 
#      were not true, then try this condition".
math = int(input("Enter Maths Marks : "))

eng = int(input("Enter English Marks : "))

comp = int(input("Enter Computer Marks : "))

mean = mean([math, eng, comp])

print('-'*50)
print(f"----- MEAN MARKS IS : {mean} --------")
print('-'*50)

if mean >= 70:
    print("Excellent Performance!")
elif mean >= 50 and mean<=69:
    print("Met expectations")
else:
    print("Below expecration")


# if...else, and & or
if mean >= 70 and math >= 70 and comp >= 70:
    print("CONGRATULATIONS! You have qualified for an IT course!")
elif mean >= 50 and math >= 55 or eng >= 60:
    print("You have qualified for a place in the University!")
else:
    print("You have qualified for an artisan course!")


# if statements cannot be empty, but if you for some reason have an if statement 
# with no content, put in the pass statement to avoid getting an error.

a = 23
b = 100
if a  < b:
    pass

# Shorthand if:
if b > a: print("a is greater than b")

# Shorthand if... else
# This technique is known as Ternary Operators, or Conditional Expressions.
print("A") if a > b else print("B")

# Shorthand if...else with multiple conditions
print("A") if a > b else print("=") if a == b else print("B")

# THE END

