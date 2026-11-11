#Python - Add List Items

#To add an item to the end of the list, use the append() method:

#Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To insert a list item at a specified index, use the insert() method.

#The insert() method inserts an item at the specified index:

#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#To append elements from another list to the current list, use the extend() method.

#The appended list elements will be added to the end of the list.

#Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#The extend() method does not have to append lists,
# you can add any iterable object (tuples, sets, dictionaries etc.).

#Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Python - Remove List Items

#The remove() method removes the specified item.

#Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#If there are more than one item with the specified value,
# the remove() method removes the first occurrence:

#Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index.
#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.
#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #This throws Error because list is deleted

#The clear() method empties the list.
#The list still remains, but it has no content.

#Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Python - Loop Lists

#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
print("****************************************************")
#You can also loop through the list items by referring to their index number.

#Use the range() and len() functions to create a suitable iterable.

#Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
print("****************************************************")

# Using a While Loop
# You can loop through the list items by using a while loop.
# Use the len() function to determine the length of the list,
# then start at 0 and loop your way through the list items by referring to their indexes.
# Remember to increase the index by 1 after each iteration.

#Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("****************************************************")

#List Comprehension offers the shortest syntax for looping through lists
#A shorthand for loop that will print all items in a list

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
print("****************************************************")

#Python - List Comprehension
# List-Comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list,
# containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
print("****************************************************")
#With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
print("****************************************************")

#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
print("****************************************************")

#The iterable can be any iterable object, like a list, tuple, set etc.

#You can use the range() function to create an iterable:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in range(10)]
print(newlist)
print("****************************************************")

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
#Return "orange" instead of "banana":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
print("****************************************************")
#The expression in the example above says:
#"Return the item if it is not banana, if it is banana return orange".


