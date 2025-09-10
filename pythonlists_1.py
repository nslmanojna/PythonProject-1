#Python Lists
# #Lists are used to store multiple items in a single variable.
#
# Lists are one of 4 built-in data types in Python used to store collections of data.
# The other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

# Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#List items are ordered, changeable, and allow duplicate values.

#List items are indexed, the first item has index [0], the second item has index [1] etc.

#When we say that lists are ordered, it means that the items have a defined order,
#and that order will not change.

#If you add new items to a list, the new items will be placed at the end of the list.

#The list is changeable, meaning that we can change, add, and remove items in a list
# after it has been created.

#Since lists are indexed, lists can have items with the same value

#Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function
print(len(thislist)) #5

#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#A list can contain different data types
#A list with strings, integers and boolean values
list1 = ["abc", 34, True, 40, "male"]

#From Python's perspective, lists are defined as objects with the data type 'list'
print(type(list1))

#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
print(type(thislist))


#Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#Access List Items

# List items are indexed, you can access them by referring to the index number:
# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana

#Negative indexing means start from the end
#-1 refers to the last item, -2 refers to the second last item etc.

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) #cherry

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#Prints n to n-1 items #['cherry', 'orange', 'kiwi']

#By leaving out the start value, the range will start at the first item
#By leaving out the end value, the range will go on to the end of the list
print(thislist[:4]) #['apple', 'banana', 'cherry', 'orange']
print(thislist[4:]) #['kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) #['orange', 'kiwi', 'melon']

#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,

#To determine if a specified item is present in a list use the in keyword:

#Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# To insert a new list item, without replacing any of the existing values,
# we can use the insert() method.
# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Python - Change List Items

#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#To insert a new list item, without replacing any of the existing values,
# we can use the insert() method.
#The insert() method inserts an item at the specified index:

#Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

