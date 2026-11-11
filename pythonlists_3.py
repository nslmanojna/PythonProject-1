#Python - Sort Lists
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

#Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
print("**************************************************************************")

#Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
print("**************************************************************************")

#Sort the list descending:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
print("**************************************************************************")

#You can also customize your own function by using the keyword argument key = function.

#The function will return a number that will be used to sort the list (the lowest number first):

#Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50) #Both Negative, Positive returns as positive

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #[50, 65, 23, 82, 100]
#50 equals 50, Next close no 65(15 difference), Next close no 23(27 difference),
# Next close no 82(32 difference), Next close no 100(50 difference)
print(thislist)
print("**************************************************************************")

#By default the sort() method is case sensitive,
# resulting in all capital letters being sorted before lower case letters:

#Case-sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
print("**************************************************************************")
#Solution to above result
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
print("**************************************************************************")

#The reverse() method reverses the current sorting order of the elements.
#Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
print("**************************************************************************")

#Python - Copy Lists
#You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.
#You can use the built-in List method copy() to copy a list.

#Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
print("**************************************************************************")

#Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
print("**************************************************************************")

#Make a copy of a list with the : operator:

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)
print("**************************************************************************")

#Python - Join Lists
#Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
print("**************************************************************************")

#Another way to join two lists is by appending all the items from list2 into list1, one by one:
#Append list2 into list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
print("**************************************************************************")

#Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
print("**************************************************************************")


#Python - List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

