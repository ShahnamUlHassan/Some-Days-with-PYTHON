# -------------------------------
# Example 1: Basic Multiplication Table (without error handling)
# -------------------------------

# Take input from user
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

# Print multiplication table from 1 to 10
for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a) * i}")

# These lines will always execute after the loop
print("Some important lines of code")
print("End of program")



# -------------------------------
# Example 2: Multiplication Table (with error handling)
# -------------------------------

# Take input from user
a = input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    # Try converting input to integer and printing the table
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a) * i}")

# Catch any general error (e.g., user enters a non-numeric value)
except Exception as e:
    print("Error:", e)

# These lines execute whether or not there was an error
print("Some important lines of code")
print("End of program")



# -------------------------------
# Example 3: Multiple Exception Handling
# -------------------------------

try:
    # Ask user for an integer
    num = int(input("Enter an integer: "))
    
    # Define a list with 2 elements
    a = [6, 2]
    
    # Try to print element at index 'num'
    print(a[num])

# Handle case when user enters non-integer input
except ValueError:
    print("Number entered is not an integer")  

# Handle case when user enters an invalid index (like 5 or -3)
except IndexError:
    print("Index error")  
