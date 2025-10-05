# -----------------------------
# Basic Dictionary Example
# -----------------------------

# A dictionary stores data in key-value pairs
dic = {
    "Shahnam": "Human being",
    "Spoon": "Object"
}
print(dic)                 # Prints the whole dictionary
print(dic["Shahnam"])      # Access value using key → Output: Human being


# -----------------------------
# Dictionary with Integer Keys
# -----------------------------
dic2 = {
    344: "Shahnam",
    56: "Hassan",
    765: "Moon",
    13: "MrBean"
}
print(dic2[13])            # Access value by key 13 → Output: MrBean


# -----------------------------
# Dictionary with Mixed Data Types
# -----------------------------
info = {"name": "Shahnam", "age": 27, "eligible": True}
print(info)                # Print the whole dictionary
print(info["name"])        # Access value by key → Output: Shahnam
print(info.get("eligible"))# Safer way to get value (won’t cause error if key not found)


# -----------------------------
# Getting Keys and Values
# -----------------------------
info = {"name": "Shahnam", "age": 27, "eligible": True}
print(info)                # Print dictionary
print(info.keys())         # Returns all keys in the dictionary
print(info.values())       # Returns all values in the dictionary

# Loop through keys
for key in info.keys():
    # Use f-string to display both key and its value
    print(f"The value corresponding to the key '{key}' is {info[key]}")


# -----------------------------
# Getting Key-Value Pairs Using items()
# -----------------------------
info = {"name": "Shahnam", "age": 27, "eligible": True}
print(info.items())        # Returns a list of (key, value) tuples

# Loop through both key and value together
for key, value in info.items():
    print(f"The value corresponding to the key '{key}' is {value}")
