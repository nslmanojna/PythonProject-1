#Python Booleans
#Booleans represent one of two values: True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)

#Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return
print(bool("Hello")) #True
print(bool(15)) #True
print(bool(1)) #True
print(bool(0)) #False

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
#In fact, there are not many values that evaluate to False, except empty values,
# such as (), [], {}, "", the number 0, and the value None.
# And of course the value False evaluates to False.

# One more value, or object in this case, evaluates to False, and that is if you have
# an object that is made from a class with a __len__ function that returns 0 or False:
# Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

def myFunction() :
  return 0
if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value, like the
# isinstance() function, which can be used to determine if an object is of a certain data type:
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))

x = 200.00
print(isinstance(x, int))