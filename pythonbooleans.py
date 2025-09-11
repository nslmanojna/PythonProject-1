# Python Booleans
# Bool represent one of two values: True or False.
"""
This file explains the usage of Python Booleans concept
"""

A = 10
B = 9
print(A > B)
print(A == B)
print(A < B)

# Print a message based on whether the condition is True or False:
NUM_1 = 200
NUM_2 = 33

if NUM_2 > NUM_1:
    print("num_2 is greater than num_1")
else:
    print("num_2 is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello"))  # True
print(bool(15))  # True
print(bool(1))  # True
print(bool(0))  # False

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
# In fact, there are not many values that evaluate to False, except empty values,
# such as (), [], {}, "", the number 0, and the value None.
# And of course the value False evaluates to False.


# One more value, or object in this case, evaluates to False, and that is if you have
# an object that is made from a class with a __len__ function that returns 0 or False:
# Example
class MyClass:
    """
    This class returns Boolean value False
    because __len__ returns 0.
    """
    def __len__(self):
        """Usage of Booleans in len() function """
        return 0
    def my_function(self):
        """Usage of Booleans in user defined function """
        return  True

# Create an object of MyClass
myobj = MyClass()
print("Boolean value of myobj:", bool(myobj))  # Output: False
print("*****************")
print(myobj.my_function())
print("*********************")

# First function
def my_function_true():
    """This method explain the usage of Bool value True"""
    return True

if my_function_true():
    print("YES!")
else:
    print("NO!")

# Second function
def my_function_false():
    """This method explain the usage of Bool value False"""
    return 0  # 0 is treated as False

if my_function_false():
    print("YES!")
else:
    print("NO!")

# Python also has many built-in functions that return a boolean value, like the
# isinstance() function, which can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:

INTNUM = 200
print(isinstance(INTNUM, int))

FLOATNUM= 200.00
print(isinstance(FLOATNUM, int))
