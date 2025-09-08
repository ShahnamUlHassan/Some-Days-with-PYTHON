# ----- Example 1: Basic String Variables -----

# Variable 'name' mein ek string store ki
name = "Shahnam"  

# Variable 'friend' mein ek string store ki
friend = "Hassan"  

# Variable 'anotherfriend' mein ek string store ki
anotherfriend = "Moon"  

# String ko print karte waqt dusre text ke sath concatenate karna
print("Hello", name)   # Output: Hello Shahnam  

# String indexing: name[0] ka matlab hai pehla character
print(name[0])   # Output: S



# ----- Example 2: String with Quotes -----

# Jab string ke andar double quotes use karne ho to single quotes se string define karte hain
apple = 'He said: "I want to eat apple'  

# Puri string print karna
print(apple)  
# Output: He said: "I want to eat apple



# ----- Example 3: Iterating Over String -----

print("Lets use a for loop\n")  

# String define ki
apple = "Hello World!"  

# Har character ko ek ek karke print karna
for chraracter in apple:  
    print(chraracter)  

# Har iteration mein poori string print hogi (12 bar print hoga)
for chraracter in apple:  
    print(apple)  
