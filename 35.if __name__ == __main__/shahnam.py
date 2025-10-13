# Defining a function named 'welcome' that prints a greeting message
def welcome():
    print("Hello you are welcome from shahnam")

# The below condition checks if this file is being run directly
# "__name__" is a special variable that becomes "__main__" 
# only when this file runs directly (not when imported)
if __name__ == "__main__":
    # This line runs only if 'shahnam.py' is executed directly
    welcome()
