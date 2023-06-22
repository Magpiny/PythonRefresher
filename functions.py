"""
    # A function is a block of code which only runs when it is called.
    # You can pass data, known as parameters, into a function.
    # A function can return data as a result

    The keyword def introduces a function definition. It must be followed by the function name 
    and the parenthesized list of formal parameters. The statements that form the body of the 
    function start at the next line, and must be indented.

    e.g def funcname(optional parameter(s)):
            indented stametements
"""

# fibonacci function
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# calling a function  --> funcname(optional argument(s))
fib(30)


# Keyword arguments : time is a keyword argument in the second greetings call
# DEFAAULT PARAMETERS: name has a default parameter 'sam'

def greetings(time,name="Sam"):
    print(f"Good {time} {name}")

greetings("evening")
greetings(time="morning", name="John")


# Parameter vs Arguments?
"""
From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

"""
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * 
before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

Arbitrary Arguments are often shortened to *args in Python documentations.
"""
def myfav(*subjects):
    print(f"My second favorite subject in highschool was {subjects[1]}")

myfav("Chemistry", "Physics", "Maths")


"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items
accordingly:

The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
"""
def login(**credentials):
    passcode = int(input("Enter password : "))
    username = input("Enter username : ")
    if passcode == 1234 and username == "sam":
        print(f"Welcome {credentials['role']} {username}")
    else:
        print("Wrong password or username!")

login(role="Admin")

"""
    The pass statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
"""
def passfunc():
    pass

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\nRecursion Example Results")
tri_recursion(6)



# LAMBDA EXPRESSION
"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

SYNTAX: lambda arguments : expression
"""
addtwonumbers = lambda a, b : a + b
print(addtwonumbers(3, 7))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
def getsqr(number):
  return lambda power : number**power

num = getsqr(2)
print(num(3))


# END OF FILE (EOF)
