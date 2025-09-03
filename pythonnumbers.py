# There are three numeric types in Python:
#
# int
# float
# complex
# Variables of numeric types are created when you assign a value to them

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

z = -87.7e100
print(z)
print(type(z))

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

#Generate random number between 1 and 10
import random

print(random.randrange(1, 10))

print(random.randrange(10))