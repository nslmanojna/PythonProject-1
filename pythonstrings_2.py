#Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!" #The first character has index 0.
print(b[7:12]) #prints n to n-1 characters

#By leaving out the start index, the range will start at the first character:

b = "Hello, World!"
print(b[:5])

#By leaving out the end index, the range will go to the end
b = "Hello, World!"
print(b[2:])

#Use negative indexes to start the slice from the end of the string
b = "Hello, World!"
print(b[-5:-2]) #prints n-1 to n characters


