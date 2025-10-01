# Example 1: Using break in for loop
for i in range(12):   # Loop 0 se 11 tak chalega
    if(i == 10):      # Jab i ki value 10 ho jaye
        break         # Loop foran band ho jayega
    # Ye tab tak chalega jab tak i < 10 hai
    print("5 X", i+1, "=", 5 * (i + 1))

print("loop ko chor kar nikal gya")  # Jab break hoga to ye execute hoga


# Example 2: Using continue in for loop
for i in range(12):   # Loop 0 se 11 tak chalega
    if(i == 10):      # Jab i ki value 10 ho jaye
        print("skip the iteration")
        continue      # Ye iteration skip ho jayegi, loop agli value par chalega
    print("5 X", i, "=", 5 * i)  # Ye tab chalega jab i != 10 hai


# Example 3: Using break in while loop
i = 0
while True:           # Infinite loop (jab tak break na ho)
    print(i)
    i = i + 1
    if(i % 10 == 0):  # Agar i ka multiple of 10 ho
        break         # Loop ko yahan band kar do
