# ----------------------------------------
# Example: Using try-except-finally with return values
# ----------------------------------------

def func():
    try:
        # Define a list
        l = [1, 5, 3, 7]

        # Ask user to enter an index number
        i = int(input("Enter the index: "))

        # Try to print the element at the given index
        print(l[i])

        # If everything works fine, return 1
        return 1

    # This block runs if any error occurs (like invalid input or index out of range)
    except:
        print("Some error occurred")

        # Return 0 if there was an error
        return 0

    # The 'finally' block runs every time — no matter what happens above
    finally:
        print("I am always executed")


# Call the function and store its return value in variable 'x'
x = func()

# Print the return value of the function
print(x)
