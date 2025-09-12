# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
"""
Python Tuples concept practice examples
"""
# Create a Tuple:

this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print("*******************************************************")
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0],
# the second item has index [1] etc.
# Ordered:
# When we say that tuples are ordered, it means that the items have a defined order,
# and that order will not change.
# Unchangeable:
# Tuples are unchangeable, meaning that we cannot change,
# add or remove items after the tuple has been created.
# Allow Duplicates:
# Since tuples are indexed, they can have items with the same value:

# Tuples allow duplicate values:

this_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(this_tuple)
print("*******************************************************")

#Print the number of items in the tuple:

this_tuple = ("apple", "banana", "cherry")
print(len(this_tuple))
print("*******************************************************")

# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.

# One item tuple, remember the comma:

this_tuple = ("apple",)
print(type(this_tuple))

#NOT a tuple
this_tuple = ("apple")
print(type(this_tuple))
print("*******************************************************")

# Tuple items can be of any data type:
# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

#Using the tuple() method to make a tuple:

this_tuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(this_tuple)
print("*******************************************************")

# There are four collection data types in the Python programming language:
#
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Python - Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# Print the second item in the tuple:

this_tuple = ("apple", "banana", "cherry")
print(this_tuple[1])
print("********************************************************************")

# Negative indexing means start from the end.
# -1 refers to the last item, -2 refers to the second last item etc.

# Print the last item of the tuple:

this_tuple = ("apple", "banana", "cherry")
print(this_tuple[-1])
print("********************************************************************")

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.
#By leaving out the start value, the range will start at the first item:
#By leaving out the end value, the range will go on to the end of the tuple:
# Return the third, fourth, and fifth item:

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[2:5])
print("********************************************************************")

# This example returns the items from index -4 (included) to index -1 (excluded)

this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(this_tuple[-4:-1])
print("********************************************************************")

# To determine if a specified item is present in a tuple use the in keyword:

# Check if "apple" is present in the tuple:

this_tuple = ("apple", "banana", "cherry")
if "apple" in this_tuple:
  print("Yes, 'apple' is in the fruits tuple")
print("********************************************************************")

#Python - Update Tuples:
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.
# But there are some workarounds.
# Once a tuple is created, you cannot change its values. Tuples are unchangeable,
# or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list,
# change the list, and convert the list back into a tuple.

# Convert the tuple into a list to be able to change it:

X = ("apple", "banana", "cherry")
Y = list(X)
Y[1] = "kiwi"
X = tuple(Y)
print(X)
print("********************************************************************")

# Since tuples are immutable, they do not have a built-in append() method,
# but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple,
# you can convert it into a list, add your item(s), and convert it back into a tuple.

# Convert the tuple into a list, add "orange", and convert it back into a tuple:

this_tuple = ("apple", "banana", "cherry")
Y = list(this_tuple)
Y.append("orange")
this_tuple = tuple(Y)
print("********************************************************************")

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples,
# so if you want to add one item, (or many), create a new tuple with the item(s),
# and add it to the existing tuple:

# Create a new tuple with the value "orange", and add that tuple:

this_tuple = ("apple", "banana", "cherry")
Y = ("orange",)
this_tuple += Y

print(this_tuple)
print("********************************************************************")

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround
# as we used for changing and adding tuple items:

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
this_tuple = ("apple", "banana", "cherry")
Y = list(this_tuple)
Y.remove("apple")
this_tuple = tuple(Y)
print(this_tuple)
print("********************************************************************")

#The del keyword can delete the tuple completely:
this_tuple = ("apple", "banana", "cherry")
del this_tuple
#print(this_tuple) #this will raise an error because the tuple no longer exists

