# -----------------------------------------------
# File Name: How import works.py
# Topic: Understanding how Python "import" works
# -----------------------------------------------

# --- Example 1: Importing an entire module ---
import pandas
# The 'pandas' library is used for data manipulation and analysis.
# Example: Reading a CSV file (currently just a placeholder)
pandas.read_csv('')

# --- Example 2: Importing math module and using a specific function ---
import math
# math.floor(x) rounds a decimal number down to the nearest integer
print(math.floor(4.232))


# --- Example 3: Importing specific functions from a module ---
from math import sqrt, pi
# sqrt(9) returns 3, and pi is a constant (~3.14159)
result = sqrt(9) * pi
print(result)


# --- Example 4: Importing all functions from a module ---
from math import *
# Now we can directly use sqrt() and pi without 'math.'
result = sqrt(9) * pi
print(result)


# --- Example 5: Using alias (nickname) for imported items ---
from math import pi, sqrt as s
# Here, 'sqrt' is renamed as 's' for short usage
result = s(9) * pi
print(result)


# --- Example 6: Giving a module an alias name ---
import math as m
# 'm' acts as a shortcut for the 'math' module
result = m.sqrt(9) * m.pi
print(result)


# --- Example 7: Exploring module contents ---
import math
# dir(module) lists all available attributes and functions inside a module
print(dir(math))
# Example of accessing 'math.nan' (Not a Number constant)
print(math.nan, type(math.nan))


# --- Example 8: Importing from a custom module (local file) ---
# Custom module 'shahnam.py' should exist in the same folder

from shahnam import welcome, shahnam
welcome()
print(shahnam)


# --- Example 9: Importing everything from a module ---
from shahnam import *
welcome()
print(shahnam)


# --- Example 10: Importing module with alias ---
import shahnam as sh
sh.welcome()
print(sh.shahnam)
