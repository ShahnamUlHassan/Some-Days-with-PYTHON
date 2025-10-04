# -----------------------------
# Set Union
# -----------------------------
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))   # Combines both sets and removes duplicates → {1, 2, 3, 5, 6, 7}
print(s1, s2)         # Original sets remain unchanged
s1.update(s2)         # Updates s1 by adding all elements of s2 into it


# -----------------------------
# Union with Cities
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities2 = {"lahore", "islamabad", "rawalpindi", "faisalabad"}
cities3 = cities.union(cities2)   # Union → combines both sets without duplicates
print(cities3)


# -----------------------------
# Intersection of Sets
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities2 = {"lahore", "islamabad", "rawalpindi", "faisalabad"}
cities3 = cities.intersection(cities2)  # Common elements only
print(cities3)


# -----------------------------
# Intersection Update
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities2 = {"lahore", "islamabad", "rawalpindi", "faisalabad"}
cities.intersection_update(cities2)   # Keeps only common elements in 'cities'
print(cities)


# -----------------------------
# Symmetric Difference
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities2 = {"lahore", "islamabad", "rawalpindi", "faisalabad"}
cities3 = cities.symmetric_difference(cities2)   # Elements that are NOT common
print(cities3)


# -----------------------------
# Disjoint Sets Check
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities2 = {"lahore", "islamabad", "rawalpindi", "faisalabad"}
print(cities.isdisjoint(cities2))  # False → because they share some cities


# -----------------------------
# Superset & Subset
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities2 = {"lahore", "islamabad"}
print(cities.issuperset(cities2))  # True → 'cities' contains all of 'cities2'

cities3 = {" rawalpindi", "multan"}
print(cities.issuperset(cities3))  # False → 'rawalpindi' (with space) is different
print(cities3.issubset(cities))    # False → not fully contained in 'cities'


# -----------------------------
# Add Elements
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities.add("multan")   # Adds new element
print(cities)


# -----------------------------
# Remove Elements
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities.remove("rawalpindi")  # Removes element (error if not found)
print(cities)


# -----------------------------
# Discard Elements
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities.discard("rawalpindi")   # Removes element (NO error if not found)
print(cities)
cities.discard("rawalpindi2")  # No error even if element doesn't exist
print(cities)


# -----------------------------
# Pop Elements
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
item = cities.pop()   # Removes and returns a random element
print(cities)
print(item)


# -----------------------------
# Delete Entire Set
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
del cities   # Deletes the set completely


# -----------------------------
# Clear Set
# -----------------------------
cities = {"karachi", "lahore", "islamabad", "rawalpindi"}
cities.clear()   # Removes all elements but keeps empty set


# -----------------------------
# Membership Test
# -----------------------------
info = {"karachi", 19, False, 5.9}
if "karachi" in info:        # Check if element exists in set
    print("karachi is present")
else:
    print("karachi is not present")
