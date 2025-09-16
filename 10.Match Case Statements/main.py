# Python program to demonstrate match-case statements
# match-case was introduced in Python 3.10

# Taking input from user
x = int(input("Enter the value of x: "))

# Match-case statement starts
match x:
    # If x == 0
    case 0:
        print("x is zero")
    
    # If x == 4
    case 4:
        print("x is 4")

    # If x is not equal to 90 (guard condition)
    case _ if x != 90:
        print(x, "is not 90")

    # If x is not equal to 80 (guard condition)
    case _ if x != 80:
        print(x, "is not 80")

    # Default case: agar koi case match na ho
    case _:
        print("Default case: x =", x)
