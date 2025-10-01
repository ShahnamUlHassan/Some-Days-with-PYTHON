# Example 1: Simple list and accessing elements
marks = [3, 5, 7]
print(marks)        # Prints the whole list: [3, 5, 7]
print(type(marks))  # Prints <class 'list'>
print(marks[0])     # Access first element → 3
print(marks[1])     # Access second element → 5
print(marks[2])     # Access third element → 7


# Example 2: Negative indexing and different ways to access elements
marks = [7, 5, 3, 1, 9]

print(marks[-3])           # Negative indexing → 3rd element from last = 3
print(marks[len(marks)-3]) # len=5 → 5-3=2 → marks[2] = 3
print(marks[5-3])          # 5-3=2 → marks[2] = 3
print(marks[2])            # Direct index 2 → 3



# Example 3: Membership check (using "in" keyword)
marks = [1, 3, 5, 7, 9]

if 6 in marks:
    print("Yes")
else:
    print("No")   # Output → No (kyunki 6 list me nahi hai)



# Example 4: List slicing
marks = [1, 3, 5, 7, 9]
print(marks)        # Prints the whole list → [1, 3, 5, 7, 9]
print(marks[1:-1])  # From index 1 to second last → [3, 5, 7]
print(marks[1:4])   # From index 1 to 3 → [3, 5, 7]



# Example 5: List comprehension
lst = [i*i for i in range(4)]
print(lst)   # Output: [0, 1, 4, 9]
