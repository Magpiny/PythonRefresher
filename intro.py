"""sumary_line
    Author: Samuel Wanjare
    Date: Wed 31st May 2023
    Title: Relearning Python the right way
    Python Verion: 3:10:10 Mar 5 2023 22:26:53
INTRO:
    What is Python?
    Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

    It is used for:

    web development (server-side),
    software development,
    mathematics,
    system scripting.

    What can Python do?

    Python can be used on a server to create web applications.
    Python can be used alongside software to create workflows.
    Python can connect to database systems. It can also read and modify files.
    Python can be used to handle big data and perform complex mathematics.
    Python can be used for rapid prototyping, or for production-ready software development.
   
    Why Python?

    Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
    Python has a simple syntax similar to the English language.
    Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
    Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
    Python can be treated in a procedural way, an object-oriented way or a functional way.

    Python is an interpreted language, which can save you considerable 
    time during program development because no compilation and linking is necessary. 

    By the way, the language is named after the BBC show “Monty Python’s Flying Circus” and 
    has nothing to do with reptiles.

The zen of python
    import this

"""
# Strings
name="Samuel Wanjare"
country=str("Kenya")
print(f"STRING INTRO: I am {name} from {country}")

#numbers
age = 33
days=int('33')

price=float(150)
new_price=120.50
PI = 3.142

opinion=bool(0)
isMarried=True
print(f"INTEGERS: age: {age} days:{days} FLOATS: price:{price} nprice: {new_price} BOOLEAN: opinion: {opinion} status: {isMarried}")

# converting binary, octal & hexadecimal to decimal
# binary
three = 0b011

# octal
nine = 0o011

# hexadecimal
seventeen=0x0011

# convert 256 base 10 to binary,octal and hexadecimal
dnum = 256

bnum = bin(dnum)
octnum = oct(dnum)
hexnum = hex(dnum)

print(f"256 to binary: {bnum}, octal: {octnum}, hexadecimal: {hexnum}")

# PYTHON COLLECTIONS(ARRAYS)
    # Lists
    # Tuples
    # Set
    # Dictionaries

# Compound data types
# Lists might contain items of different types, but usually the items all  
# have the same type.
# List items are ordered, changeable, and allow duplicate values.
list = [12,2,3,4,5,89,44]

# Dictionary
new_dict = {"name": "Dictionary", "like":"Javascript Object"}


# Tuple
new_tuple = {123, False, "tuple"}

# Set
new_set = ("abc", True, 4059)

"""
PYTHON CODING STYLE :PEP 8

Use 4-space indentation, and no tabs.

4 spaces are a good compromise between small indentation (allows greater nesting depth) and large 
indentation (easier to read). Tabs introduce confusion, and are best left out.

Wrap lines so that they don’t exceed 79 characters.

This helps users with small displays and makes it possible to have several code files side-by-side on 
larger displays.

Use blank lines to separate functions and classes, and larger blocks of code inside functions.

When possible, put comments on a line of their own.

Use docstrings.

Use spaces around operators and after commas, but not directly inside bracketing constructs: 
a = f(1, 2) + g(3, 4).

Name your classes and functions consistently; the convention is to use UpperCamelCase for classes 
and lowercase_with_underscores for functions and methods. Always use self as the name for the first 
method argument (see A First Look at Classes for more on classes and methods).

Don’t use fancy encodings if your code is meant to be used in international environments. Python’s 
default, UTF-8, or even plain ASCII work best in any case.

Likewise, don’t use non-ASCII characters in identifiers if there is only the slightest chance people speaking a different language will read or maintain the code.

"""
