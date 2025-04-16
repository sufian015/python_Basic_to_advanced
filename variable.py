
## Variable(container)

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

a= 5
print(a)

x = "Python is amazing"
print(x)


# Variables do not need to be declared with any particular type, and can even change type after they have been set

name= 4
name="something"
print(name) # That output is something


# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)


# You can get the data type of a variable with the type() function.

x = 4
y= "Jamir"

print(type(x))
print(type(y))


# Case-Sensitive
# Variable names are case-sensitive.

a= 5
A='hello'
print(a)
print(A)

#A will not overwrite a

# Note:Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

## Python allows you to assign values to multiple variables in one line:

name,gender,job='moon',27,'marketing'
print(name)
print(gender)
print(job)

# And you can assign the same value to multiple variables in one line:


x = y = z = "Orange"
print(x)
print(y)
print(z)


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

name= 'jamir', 'tasnim', 'sifat'

a,b,c=name

print(a)
print(b)


# In the print() function, you output multiple variables, separated by a comma

# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.


x="someone"

def my_name():
     print(x)

my_name()



