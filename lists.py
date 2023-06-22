mylist = [23, 34, 56, 89, 45, 19]
# Getting first item
mylist[-1]
#Getting last item
mylist[-2]
#Adding an item to the end of the lis
mylist.append(17)
# Getting all list items
mylist[:]
# Getting the last three items
mylist[-4:]
# Get values between range 
mylist[1:5]
# change the value of a lis
mylist[2]=45

# LIST METHODS
# remove

# list.remove(56)
mylist.pop()

# add
mylist.insert(2, 100)

# Extend list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(f"Extended List: {thislist}")

# Getting the length of the list
print(f"This list contains: {thislist}")
print(f"There are {len(thislist)} items in thislist")

# Looping through lists : for and while loops can be used here
for x in tropical:
    print(x)

# LIST COMPREHENSION
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

new_list = []

# Normally
for x in thislist:
    if "a" in x:
        new_list.append(x)

print(x)

# With list comprehension
# Syntax: newlist = [expression for item in iterable if condition == True]
newlist = [x for x in thislist if "a" in x]

print("New List: ",newlist)

capList = [x.upper() for x in tropical]
print("CapList: ", capList)

# ITERABLE
# The iterable can be any iterable object, like a list, tuple, set etc.
num_list = [x for x in range(20) if x%2==0]
print(num_list) # Will print all even numbers btwn 0 & 20
thislist.sort(reverse=True)

# SORTING LISTS
print("Sorted Reverse: ", thislist)

# Copy Lists
# copy() method
copiedList=tropical.copy()
print(f"Copied List: {copiedList}")

# list() method
withlist = list(tropical)
print(f"Copied with list():  {withlist}")






