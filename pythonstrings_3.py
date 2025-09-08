#Python has a set of built-in methods that you can use on strings.
#The upper() method returns the string in upper case
#The lower() method returns the string in lower case
#The strip() method removes any whitespace from the beginning or the end
#The replace() method replaces a string with another string
#The split() method splits the string into substrings if it finds instances of the separator

a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("World", "Python"))
b="Hello,World!"
print(a.split()) #Default split by White space
print(b.split()) #Default split by White space
print(b.split(',')) #Before ',' one element,after ',' one element
print(b.split('!')) #Before '!' one element,after ',' one element(here space)

#String Concatination
#To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#String Format
# We cannot combine strings and numbers using python variables
# age = 36
#This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)
#      txt = "My name is John, I am " + age
#            ~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
#  TypeError: can only concatenate str (not "int") to str

#But we can combine strings and numbers by using f-strings or the format() method!
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)

#A placeholder can contain variables, operations, functions, and modifiers to format the value.
#A placeholder can include a modifier to format the value.

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f
# which means fixed point number with 2 decimals:

#Display the price with 2 decimals:

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#Perform a math operation in the placeholder, and return the result:

txt = f"The price is {20 * 59} dollars"
print(txt)

