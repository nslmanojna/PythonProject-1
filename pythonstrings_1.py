# PythonStrings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# # 'hello' is the same as "hello".
#print("Hello") is Same as print('Hello')
# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) #or ''' ''' in place of """ """

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
#
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
#
# Square brackets can be used to access elements of the string.
#
# Example
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1]) #Output: e

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)

#The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

#To check if a certain phrase or character is NOT present in a string, we can use
# the keyword 'not in'
txt = "The best things in life are free!"
print("expensive" not in txt)

