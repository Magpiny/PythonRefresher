"""
OOP has been covered in classes file but it will not cause any harm trying it out one more time
"""
from decorator import add

@add
def newaddfn(*args):
        print("Hello world")

newaddfn([1,2,3, 22,33,44,55])

