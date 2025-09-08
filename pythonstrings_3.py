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
#You will get an error if you use double quotes inside a string that is surrounded by double quotes
#txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" from the north." # This is correct

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning