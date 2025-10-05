# ----------------------------------------
# Example: Raising Custom Errors in Python
# ----------------------------------------

# Ask user to enter a number
a = int(input("Enter any value between 5 and 9: "))

# Check if the entered value is outside the allowed range (5 to 9)
if a < 5 or a > 9:
    # Manually raise a ValueError with a custom error message
    # This is useful for enforcing input validation or custom rules
    raise ValueError("Value should be between 5 and 9")

# If the value is valid (within 5 and 9), print confirmation
print("You entered a valid number:", a)
