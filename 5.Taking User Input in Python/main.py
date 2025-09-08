# ----- Example 1: Taking String Input -----

# User se name input lena (default input type string hota hai)
a = input("Enter your name: ")  

# User ka naam print karna
print("My name is", a)  



# ----- Example 2: Taking Numeric Input -----

# User se pehla number input lena (ye string return karega)
x = input("Enter your 1st num: ")  

# User se doosra number input lena (ye bhi string return karega)
y = input("Enter your 2nd num: ")  

# Dono strings ko int mein typecast karke addition karna
print(int(x) + int(y))  
