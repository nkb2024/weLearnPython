#Data Types
#In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.
#Python has the following data types built-in by default, in these categories:
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
x = "Hello World"	#str
print(x.split('H'))
x = 20	#int
print(x)
x = 20.5	#float
print(x)
x = 1j	#complex
print(x)
x = ["apple", "banana", "cherry"]	#list
x = ("apple", "banana", "cherry")	#tuple
x = range(6)	#range
x = {"name" : "John", "age" : 36}	#dict
x = {"apple", "banana", "cherry"}	#set
x = frozenset({"apple", "banana", "cherry"})	#frozenset
x = True	#bool
x = b"Hello"	#bytes
x = bytearray(5)	#bytearray
x = memoryview(bytes(5))	#memoryview
x = None	#NoneType
#Python String format() Method
#The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)