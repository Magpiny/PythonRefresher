"""
Decorators
    By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.

SYNTAX:
    @dec2
    @dec1
    def func(arg1, arg2, ...):
         pass

"""
import functools

# GETTING STARTED
def add_nums(num1, num2):
    nsum = num1+num2
    return f"num1 + num2 = {nsum}"

def mult_nums(num1, num2):
    prod = num1 * num2
    return f"num1 x num2 = {prod}"

def higherorderfunc(add_or_mult_func):
    return add_or_mult_func(4,5)

print(higherorderfunc(add_nums)) # num1 + num2 = 9

print(higherorderfunc(mult_nums)) # num1 * num2 = 20

# version 2
def mydecorator(newfunc):
    def wrapper():
        print("Before function call")
        newfunc()
        print("After func call")
    return wrapper

def hello():
    print("Hello from decorator function".rjust(4, " "))

greetings = mydecorator(hello)

greetings()

# VERSION 3
"""
So, @my_decorator is just an easier way of saying greetings = mydecorator(hello). It’s how you apply a decorator to a function.
"""
def newdeco(func):
    def wrapper(*args, **kwargs):
        print("STart new decorator")
        func(*args, **kwargs)
        print("End decorator ") 

    return wrapper

@newdeco
def dfunc(name):
    print(f"Hello {name}, this is a decorated fucntion", end="\n")

dfunc("Sam")

# addition decorator
def add(add_func):
    @functools.wraps(add_func)
    def wrapper(*args):
        # add_func(*args)
        print(f"sum of {len(*args)} numbers is {sum(*args)}")
        return add_func(*args)
    return wrapper

# Decorating classes
"""
Some commonly used decorators that are even built-ins in Python are @classmethod, 
@staticmethod, and @property. The @classmethod and @staticmethod decorators are used 
to define methods inside a class namespace that are not connected to a particular 
instance of that class. The @property decorator is used to customize getters and 
setters for class attributes. 
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535





