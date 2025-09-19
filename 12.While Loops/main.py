# Example 1: For loop with range
# range(5) -> 0 se 4 tak numbers generate karega
for i in range(5):
    print(i)


# Example 2: While loop
# Jab tak i < 5 hai, loop chalega
i = 0
while(i < 5):
    print(i)
    i = i + 1   # Har step par i ko 1 se increase karna
print("Done with the loop")   # Jab condition false ho jaye to loop band


# Example 3: While loop with user input
# Yeh tab tak chalega jab tak user input <= 38 hoga
i = int(input("Enter the number: "))
while(i <= 38):
    i = int(input("Enter the number: "))   # Har baar naya input lena
    print(i)

print("Done with the loop")   # Jab condition false ho jaye to yeh chalega


# Example 4: While loop countdown
# count ki value 5 se start hogi aur har baar 1 kam hoti rahegi
count = 5
while(count > 0):
    print(count)
    count = count - 1   # Decrease the count by 1 each time


# Example 5: While loop with else
# Jab condition false ho jaye (count == 0), else part run hoga
count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("Im inside the else")
