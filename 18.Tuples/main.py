# Example: Tuple basics
tup = (1, 5, 3, 9, 2)

print(type(tup))   # <class 'tuple'> (tuple data type)
print(tup[0])      # Access first element → 1
print(len(tup))    # Length of tuple → 5

# Membership check
if 5 in tup:
    print("Yes 5 in this tuple")   # This will print because 5 exists

# Tuple slicing
tup2 = tup[2:4]    # Slice from index 2 to 3 → (3, 9)
print(tup2)
print(len(tup2))   # Length of new tuple → 2
