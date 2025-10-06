# Define a list of marks
marks = [12, 21, 32, 41, 54, 45, 19, 39]

# Initialize an index counter manually
index = 0

# Loop through each mark in the list
for mark in marks:
    # Print each mark
    print(mark)
    
    # When index reaches 3 (4th item because index starts from 0)
    # print a special message for Ali
    if index == 3:
        print("Ali, Awesome!")
    
    # Increase index by 1 after each iteration
    index += 1


# Define a list of marks
marks = [12, 21, 32, 41, 54, 45, 19, 39]

# Use enumerate() to get both index and value in each iteration
for index, mark in enumerate(marks):
    # Print each mark
    print(mark)
    
    # When the index is 3 (4th mark), print a special message
    if index == 3:
        print("Ali, Awesome")


# Define a list of marks
marks = [12, 21, 32, 41, 54, 45, 19, 39]

# Use enumerate() with start=1 so index starts from 1 instead of 0
for index, mark in enumerate(marks, start=1):
    # Print each mark
    print(mark)
    
    # When the index reaches 3 (3rd item), print a special message
    if index == 3:
        print("Ali, Awesome")
