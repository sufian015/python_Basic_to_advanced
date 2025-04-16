

## Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

# Example	Data Type	

x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	
# """"""""


## Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:

# Example	Data Type	Try it

x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(["apple", "banana", "cherry"])	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview


## Python Numbers
# There are three numeric types in Python:

# int
# float
# complex
# Variables of numeric types are created when you assign a value to them:

# Example
# x = 1    # int
# y = 2.8  # float
# z = 1j   # complex

# print(type(x))
# print(type(y))
# print(type(z))




## Specify a Variable Type

# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals.

# Example

# Integers:

# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3

# # Floats:

# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2