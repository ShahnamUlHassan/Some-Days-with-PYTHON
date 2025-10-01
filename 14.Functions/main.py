# Assigning values to variables
a = 5
b = 7

# Calculating Geometric Mean (Gmean) using the formula (a*b)/(a+b)
gmean1 = (a * b) / (a + b)
print(gmean1)  # Print result of gmean1


# Assigning new values to variables
c = 8
d = 4

# Calculating Gmean again with new values
gmean2 = (c * d) / (c + d)
print(gmean2)  # Print result of gmean2


# Defining a function to calculate and print Gmean
def calculateGmean(a, b):
    # Formula for Gmean
    mean = (a * b) / (a + b)
    print(mean)  # Print result inside the function


# Calling the function with variables a and b
calculateGmean(a, b)


# Checking which number is greater
if a > b:
    print("1st number is greater")
else:
    print("2nd number is greater")
