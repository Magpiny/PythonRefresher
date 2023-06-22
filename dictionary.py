"""
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionary items are ordered, changeable, and does not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "isVehicle":True
}

# Adding new item
thisdict["country"] = "USA"
# Using the dict constructor
# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
mydict=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(mydict)

# deleting an item
# del thisdict[brand]

# Print the number of items in the dictionary
# Dictionary length
print(thisdict)
print(f"thisdict has {len(thisdict)} items")

# Accessing dictionary items
brand = thisdict["brand"]
brand1 = thisdict.get("brand") # using get
print(f"[]: {brand}, get(): {brand1}")

# Get keys
print(f"keys: {mydict.keys()} : {mydict}")

# Get values
print(f"values: {mydict.values()}")

# Change items
mydict.update({"sape": 7070})
print(mydict)

# Remove items : pop(keyname), popitems(), del & clear
# pop() : method removes the item with the specified key name

mydict.pop("sape")

# popitem(): method removes the last inserted item (in versions before 3.7, a random item is removed instead):

mydict.popitem()

# del keyword removes the item with the specified key name

del mydict["guido"]

# clear() method empties the dictionary:

mydict.clear()

# Looping through dictionary

for k, v in thisdict.items():
  print(f"{k}: {v}")

# Make a COPY of a dictionary
# Make a copy of a dictionary with the copy() method
thisdictcopy = thisdict.copy()

# Make a copy of a dictionary with the dict() function
thisdictcopy1 = dict(thisdict)

print(f"copy(): {thisdictcopy}, dict(): {thisdictcopy1}")

# Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(f"Nested dictionary: {myfamily}")
# Accessing items in a nested dictionary
print(myfamily["child2"]["name"])

# THE END
