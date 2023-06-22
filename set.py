"""
A set is an unordered collection with no duplicate elements. 
Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.

UNOREDERD, IMUTABLE, DUPLICATES NOT ALLOWED!
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
fruits = set(('mangoe', 'guava', 'coacoanut'))

print(fruits)

# Membership
print("apple" in basket) #True
print("guava" in basket) #False

# Eliminating duplicate entries
vowels = "aeiouaaeeiioouuaa"
print(set(vowels)) # {'o', 'i', 'u','a','e'}

# Mathematic operations
a = set('abracadabra')
b = set('alacazam')

# unique leters in a
print("a Unique ", a)
print((f"b Unique: {b}"))

# union -> Letters in a and b or both
print(f"UNION: {a | b}")

# intersection -> Letters in both a and b
print(f"INTERSECTION: {a & b}")

# letters in a or b but not both
print(f"DIFFERENCE: {a^b}")

# letters in a but not in b
print("Letters in a but not b",a-b)

# Set comprehension
c = {x for x in 'abracadabra' if x not in 'abc'}
print("Set comprehension", c)

# Add items to a set
# Once a set is created, you cannot change its items, but you can add new items.
# Add an Item
fruits.add("jamna")
print(f"Fruits: {fruits}")

# Add a set
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print(f"Updated fruits: {fruits}")

# Add any iterable
sth = ['stone', 'sand']
fruits.update(sth)
print(fruits, " sth")

# Remove items in a set
# Remove an item
# fruits.remove("stone")
# fruits.discard("sand")

# Remove items
# fruits.clear() empties the set
# del fruits removes the set completely

# Join sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)




