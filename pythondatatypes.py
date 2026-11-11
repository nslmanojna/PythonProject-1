# Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

string="Python"
print(string)
print(type(string))

int=50
print(int)
print(type(int))

float=198.7
print(float)
print(type(float))

complex=7j
print(complex)
print(type(complex))

list_fruits=['apple','guava','cherry']
print(list_fruits)
print(type(list_fruits))

bool = True
print(bool)
print(type(bool))

x = ("apple", "banana", "cherry")
print(type(x))
x = range(6)
print(type(x))
x = {"name" : "John", "age" : 36}
print(type(x))
x = {"apple", "banana", "cherry"}
print(type(x))
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
x = True #bool
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview
x = None	#NoneType

# x = str("Hello World")	#str
# x = int(20)  #int
# x = float(20.5)	#float
# x = complex(1j)	#complex
# x = list(("apple", "banana", "cherry"))	#list
# x = tuple(("apple", "banana", "cherry"))	#tuple
# x = range(6)	#range
# x = dict(name="John", age=36)	#dict
# x = set(("apple", "banana", "cherry"))	#set
# x = frozenset(("apple", "banana", "cherry"))	#frozenset
# x = bool(5)	#bool
# print(type(x))
# x = bytes(5)	#bytes

