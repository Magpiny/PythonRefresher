"""
© 2023 by Magpiny

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type
of object, allowing new instances of that type to be made. Each class instance can have attributes attached 
to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying 
its state.

A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries

The global statement can be used to indicate that particular variables live in the global scope and should be 
rebound there; the nonlocal statement indicates that particular variables live in an enclosing scope and should be rebound there


SYNTAX: class ClassName:
            property=121
            def method:
"""

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I am {self.name} and I am {self.age}yrs old"

new_class = MyClass("Sammy", 18)

print(new_class)
print(new_class.name)

"""
THE SELF PARAMETER
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

# Methods in python
class NewClass:
    def __init__(self, country, continent):
        self.continent = continent
        self.country = country

    def __str__(self):
        return f"{self.counry} is in {self.continent}"

    def meth(self, name):
        print(f"I am {name} from {self.country}, {self.continent}")

nclass = NewClass("Kenya", "Africa")

nclass.meth("Meshack")


# You can delete objects by using the del keyword:
# e.g del nclass.country
# or del nclass

# THE PASS STATEMENT
#class definitions cannot be empty, but if you for some reason have a class definition with no 
# content, put in the pass statement to avoid getting an error.
class NoIdea:
    pass 


# Python Inheritance
# Create Parent Class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{ self.name } is from the {self.breed} family"

    def getname(self):
        print(f"The dog's name is {self.name}")

# Create a child class and let it inherit properties of the base/parent class
class GermanShephered(Dog):
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age =age

    def get_details(self):
        print(f"{ self.name.upper()} is of type { self.breed } and he is { self.age } yrs old")

new_dog = GermanShephered("Rex", "Jackal", 3)

new_dog.get_details()

# calling inherited method
new_dog.getname()

# Polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()











