# Normal function with 2 arguments
def average(a, b):
    print("The average is ", (a+b)/2)

# Function call with values (4, 6)
average(4, 6)   # Output: The average is 5.0



# Function with default arguments
def average(a=5, b=7):
    print("The average is ", (a+b)/2)

# Call function with only one value
average(4)   # Output: The average is (4+7)/2 = 5.5



# Function with default middle name and last name
def name(fname, mname = "john", lname = "guru"):
    print("Hello", fname, mname, lname)

# Calling with 3 arguments (override defaults)
name("bravo", "sammy", "russel")  
# Output: Hello bravo sammy russel



# Another default arguments example
def average(a=2, b=4):
    print("The average is ", (a+b)/2)

# Call function with keyword arguments
average(b=9)         # Output: (2+9)/2 = 5.5   (a default=2 use hua)
average(b=9, a=21)   # Output: (21+9)/2 = 15.0 (dono values overwrite hui)
