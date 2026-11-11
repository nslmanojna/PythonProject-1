# Specify a Variable Type
# There may be times when you want to specify a type on to a variable.
# This can be done with casting.
# Python is an object-orientated language, and as such it uses classes to define data types,
# including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal
# (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal
# or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types,
# including strings, integer literals and float literals

"""
Casting in python is therefore done using constructor functions
"""

#Integers:

X = int(1)   # x will be 1
Y = int(2.8) # y will be 2
Z = int("3") # z will be 3

#Floats:

A = float(1)     # x will be 1.0
B = float(2.8)   # y will be 2.8
C = float("3")   # z will be 3.0
D = float("4.2") # w will be 4.2

#Strings:

A = str("s1") # x will be 's1'
B = str(2)    # y will be '2'
C = str(3.0)  # z will be '3.0'
