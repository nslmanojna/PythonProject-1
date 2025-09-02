#Python Variables
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

# Camel Case
# Each word, except the first, starts with a capital letter:
# myVariableName = "John"
#
# Pascal Case
# Each word starts with a capital letter:
# MyVariableName = "John"
#
# Snake Case
# Each word is separated by an underscore character:
# my_variable_name = "John"

#Mutiple Variables - Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Multiple variables - One value
x = y = z = "Orange"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables.
# This is called unpacking.

#Unpack a list:

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

# x = 5
# y = "John"
# print(x + y)

x = 5
y = "John"
print(x, y)

