# Example 1: Modifying a tuple (indirect way)

countries = ("Spain", "Italy", "Pakistan", "England", "Germany")

# Tuples are immutable (not directly changeable)
# So we convert it into a list first
temp = list(countries)

temp.append("Russia")   # Add "Russia"
temp.pop(3)             # Remove element at index 3 → removes "England"
temp[2] = "Finland"     # Replace "Pakistan" with "Finland"

# Convert back to tuple
countries = tuple(temp)
print(countries)
# Output → ('Spain', 'Italy', 'Finland', 'Germany', 'Russia')


# Example 2: Tuple method - count()

tuple = (0, 1, 2, 3, 0, 9, 8, 7, 0, 6, 5, 4, 0)

res = tuple.count(0)  # Counts how many times 0 appears
print("Count of 0 in tuple is", res)
# Output → Count of 0 in tuple is 4
