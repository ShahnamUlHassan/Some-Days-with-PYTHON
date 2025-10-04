# -----------------------------
# Working with Sets in Python
# -----------------------------

# Define a set with some duplicate values
# Note: Sets automatically remove duplicates and only keep unique values
s = {2, 4, 2, 6}
print(s)   # Output will be {2, 4, 6}

# Define another set with mixed data types
# It contains string, integer, boolean, and float
# Duplicate elements (like 19) will be stored only once
info = {"Shahnam", 19, False, 5.9, 19}
print(info)

# Creating an empty set
# Important: {} creates a dictionary, so we use set() for an empty set
moon = set()
print(type(moon))   # <class 'set'>

# Iterating through a set
# Since sets are unordered collections, the output order may vary
for value in info:
    print(value)
