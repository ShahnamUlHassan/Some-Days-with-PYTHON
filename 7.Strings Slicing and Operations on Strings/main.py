# ----- Example 1: String Slicing -----
names = "Shahnam,Hassan"  

# Index 0 se 6 tak (7 exclusive) characters print honge
# Output: "Shahnam"
print(names[0:7])  



# ----- Example 2: String Length aur Slicing -----
fruit = "Mango"  

# String ki length nikalna (total characters count)
mangoLen = len(fruit)  
print(mangoLen)   # Output: 5  

# Index 0 se 3 tak => "Mang"
print(fruit[0:4])  

# Index 1 se 3 tak => "ang"
print(fruit[1:4])  

# Agar start missing ho to by default 0 hota hai
# [:5] => "Mango"
print(fruit[:5])  

# Negative index use karke slicing
# 0 se lekar -3 tak => "Ma"
print(fruit[0:-3])  

# -3 se lekar -1 tak => "ng"
print(fruit[-3:-1])  



# ----- Example 3: Negative Slicing -----
nm = "Shahnam"  

# -4 se lekar -2 tak => "hn"
print(nm[-4:-2])  
