# A tuple is a collection which is ordered and unchangeable.
# Allow duplicate values

mytuple = ("apple", "banana", "cherry")
print(mytuple)

# length: Number of items in a tuple
print(f"mytuple has {len(mytuple)} items")

# A tuple can contain different data types:

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

newtup = 34, "hello", True
print(newtup)

# accessing values of a tuple: just like accessing array elements
print(newtup[1]) # ->hello

# Tuple Methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# count()
# The count() method returns the number of times a specified value appears in the tuple.xy=thistuple.count(8) #2
print(f"8 appeared {thistuple.count(8)} times in thistuple")

# index
# Searches the tuple for a specified value and returns the position of where it was found
x = thistuple.index(8) #3
print(f"{thistuple}: the first 8 in this tuple appears at position {thistuple.index(8)}")

# Remove item
mytuple.remove("cherry") # removes an item from a tuple
# del keyword to remove the entire tuple e.g del mytuple


