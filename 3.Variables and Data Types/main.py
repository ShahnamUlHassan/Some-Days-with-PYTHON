# Assigning an integer value to variable 'a'
a = 123
# Printing the value stored in variable 'a'
print(a)

# Assigning a string value to variable 'b'
b = "Shahnam"
# Printing the value stored in variable 'b'
print(b)

# Assigning another integer value to variable 'a1'
a1 = 2
# Printing the sum of variable 'a' and 'a1'
print(a + a1)

# Printing the type of variable 'a'
# type(a) returns <class 'int'> because 'a' stores an integer
print("The type of a is :", type(a))

# Printing the type of variable 'b'
# type(b) returns <class 'str'> because 'b' stores a string
print("The type of b is :", type(b))


# Creating a list with different types of elements
# The list contains:
#   1. An integer (8)
#   2. A floating-point number (2.3)
#   3. Another list with two integers ([-4, 5])
#   4. Another list with two strings (["apple", "bnana"])
list = [8, 2.3, [-4, 5], ["apple", "bnana"]]

# Printing the list to see its contents
print(list)

# Checking the type of 'list'
# It will return <class 'list'>
print("The type of variable 'list' is:", type(list))


# Creating a tuple that contains two inner tuples
# 1. First inner tuple has two strings: ("parrot", "sparrow")
# 2. Second inner tuple has two strings: ("lion", "tiger")
tuple = (("parrot", "sparrow"), ("lion", "tiger"))

# Printing the tuple to display its contents
print(tuple)

# Checking the type of the variable 'tuple'
# It will return <class 'tuple'>
print("The type of variable 'tuple' is:", type(tuple))


# Creating a dictionary with key-value pairs
# Keys are unique identifiers and values can be of any data type
# Dictionary contains:
#   1. "name"  -> "Shahnam" (string)
#   2. "age"   -> 27 (integer)
#   3. "canVote" -> True (boolean)
dict = {"name": "Shahnam", "age": 27, "canVote": True}

# Printing the entire dictionary
print(dict)

# Checking the type of variable 'dict'
# It will return <class 'dict'>
print("The type of variable 'dict' is:", type(dict))
