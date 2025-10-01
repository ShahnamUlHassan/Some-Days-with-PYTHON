# Example 1: Basic list methods
list = [9, 8, 1, 2, 4, 6]
print(list)        # Original list → [9, 8, 1, 2, 4, 6]

list.append(7)     # Add element at the end
print(list)        # → [9, 8, 1, 2, 4, 6, 7]

list.sort()        # Sort in ascending order
print(list)        # → [1, 2, 4, 6, 7, 8, 9]

list.sort(reverse=True)  # Sort in descending order
print(list)        # → [9, 8, 7, 6, 4, 2, 1]

list.reverse()     # Reverse the order
print(list)        # → [1, 2, 4, 6, 7, 8, 9]

print(list.index(2))   # Find index of value 2 → 1
print(list.count(6))   # Count occurrences of 6 → 1


# Example 2: Copying lists (important concept!)
list1 = [9, 8, 1, 2, 4, 6]
m = list1          # m points to the SAME list (reference copy)
m[0] = 0
print(list1)       # → [0, 8, 1, 2, 4, 6] (list1 bhi change ho gayi!)


# Example 3: True copy using copy() method
list2 = [9, 8, 1, 2, 4, 6]
m = list2.copy()   # New independent copy
print(list2)       # → [9, 8, 1, 2, 4, 6]


# Example 4: Insert element at specific position
list2 = [9, 8, 1, 2, 4, 6]
list2.insert(1, 45)    # At index 1, insert 45
print(list2)           # → [9, 45, 8, 1, 2, 4, 6]



# Example 5: Extend (add multiple values)
list2 = [9, 8, 1, 2, 4, 6]
m = [900, 1000, 1100]
list2.extend(m)        # Add all elements of m at the end
print(list2)           # → [9, 8, 1, 2, 4, 6, 900, 1000, 1100]



# Example 6: Concatenation of lists
l = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = l + l2            # Join both lists
print(l3)              # → [1, 2, 3, 4, 5, 6, 7, 8]
