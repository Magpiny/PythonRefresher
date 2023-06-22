"""
Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:
try... except ... and catch blocks


The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

# The code below should generate an exception because a is not defined

try:
    print(a**2)
except:
    print("A is not defined!")

# Many exceptions
try:
    print(b)
except NameError:
    print("No variable named b, try with multiple exceptions")
except:
    print("Unexpected error occured")

# try... except ... finally
# finally block will be executed regardless of the outcome
try:
    print(a)
except:
    print("variable k does not exist. try with finally")
finally:
    print("The code ran and ended ...finally!")



















