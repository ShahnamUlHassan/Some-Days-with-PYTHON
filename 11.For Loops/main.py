# Example 1: Looping through a string
name = "Shahnam"
print(name)   # String ko print karna

# For loop har character ko ek ek karke print karega
for i in name:
    print(i)
    if(i == "h"):   # Agar character "h" mila
       print("This is something special")


# Example 2: Looping through a list of colors
colors = ["Red", "Green", "Blue", "Orange"]
print(colors)   # List ko print karna

# For loop list ke har element ko access karega
for color in colors:
    print(color)     # Color ka naam print
    # Nested loop: color string ke har letter ko print karega
    for i in color:
        print(i)


# Example 3: Using range() function
# range(10) → 0 se 9 tak numbers generate karega
for k in range(10):
    print(k + 1)   # Print karega 1 se 10 tak


# Example 4: Using range(start, end)
# range(1, 21) → 1 se 20 tak numbers generate karega
for k in range(1, 21):
    print(k)
