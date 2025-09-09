# String Methods in Python

# Original string with extra spaces and exclamation marks
a = "Shahnam  !!!!!! !!!!!"
print(a)   # Prints the string as it is

# len() → Returns the total length (number of characters) in the string
print(len(a))   # Output: includes spaces and special characters

# upper() → Converts all characters of the string to UPPERCASE
print(a.upper())

# lower() → Converts all characters of the string to lowercase
print(a.lower())

# rstrip(chars) → Removes the specified characters (default: whitespace) 
# only from the right (end) of the string
print(a.rstrip("!"))   # Removes trailing "!" from the string

# replace(old, new) → Replaces all occurrences of the old substring with the new one
print(a.replace("Shahnam", "Hassan"))  # Replaces "Shahnam" with "Hassan"

# split(delimiter) → Splits the string into a list based on the given delimiter
# By default, it splits on spaces.
print(a.split(" "))   # Splits the string by spaces

# capitalize() → Capitalizes the first character of the string and makes the rest lowercase
blogHeading = "introduction tO js"
print(blogHeading.capitalize())   # Output: "Introduction to js"


# Another string example
str = "Welcome to console"

# len() → Again returns total length of the string
print(len(str))   # Output: 18

# center(width) → Returns a new string of specified width with the original string centered
# It fills the extra space with spaces (by default).
print(len(str.center(50)))   # Length becomes 50 because of centering

# String Methods in Python (Part 2)

# count(substring) → Returns the number of times a substring appears in the string
b = "Shahnam"
print(b.count("a"))   # Output: 2 → "a" occurs twice


# endswith(suffix) → Checks if the string ends with the given suffix
# endswith(suffix, start, end) → Checks only in the given slice of the string
str1 = "Welcome to the console!!!"
print(str1.endswith("!!!"))         # True → String ends with "!!!"
print(str1.endswith("to", 4, 10))   # True → from index 4 to 10 substring is "to"


# find(substring) → Returns the index of the first occurrence of substring
# If not found, it returns -1
str2 = "He's name is John. He is an honest man"
print(str2.find("is"))    # Output: 9 → first "is" starts at index 9
print(str2.find("ishh"))  # Output: -1 → because "ishh" is not present


# index(substring) → Works same as find(), but raises an ERROR if substring not found
print(str2.index("is"))   # Output: 9
# print(str2.index("ishh"))  # ❌ ValueError: substring not found

# String Methods in Python (Part 3)

# isalnum() → Returns True if the string consists of only letters and numbers (no spaces or symbols)
str3 = "WelcomeToTheSchool"
print(str3.isalnum())   # ✅ True → only alphabets, no spaces/symbols


# isalpha() → Returns True if the string consists of only alphabets (no digits, no spaces)
str4 = "Welcome00"
print(str4.isalpha())   # ❌ False → because it contains digits "00"


# islower() → Returns True if all characters in the string are lowercase
c = "hello world"
print(c.islower())      # ✅ True → all letters are lowercase

cc = "hello World"
print(cc.islower())     # ❌ False → "W" is uppercase


# isprintable() → Returns True if all characters are printable (no escape characters like \n, \t)
d = "We wish you a maryy christmas"
print(d.isprintable())   # ✅ True → all characters are printable

dd = "we wish you a marry christmas\n"
print(dd.isprintable())  # ❌ False → "\n" (newline) is not printable
