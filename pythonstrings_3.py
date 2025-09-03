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

