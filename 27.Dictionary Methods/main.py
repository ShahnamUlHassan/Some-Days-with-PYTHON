# -----------------------------
# Update Method
# -----------------------------
# update() merges one dictionary into another
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
ep2 = {222: 65, 566: 76}
ep1.update(ep2)   # Adds all key-value pairs from ep2 into ep1
print(ep1)        # Output: {122: 67, 657: 59, 351: 78, 513: 66, 222: 65, 566: 76}


# -----------------------------
# Clear Method
# -----------------------------
# clear() removes all key-value pairs, leaving an empty dictionary
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
ep2 = {222: 65, 566: 76}
ep1.clear()       # Removes everything from ep1
print(ep1)        # Output: {}


# -----------------------------
# Empty Dictionary
# -----------------------------
# You can also manually create an empty dictionary
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
empt = {}         # Empty dictionary
print(empt)       # Output: {}


# -----------------------------
# pop() Method
# -----------------------------
# pop(key) removes the specified key-value pair
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
ep1.pop(122)      # Removes key 122
print(ep1)        # Output: {657: 59, 351: 78, 513: 66}


# -----------------------------
# popitem() Method
# -----------------------------
# popitem() removes and returns the last inserted key-value pair
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
ep1.popitem()     # Removes the last item (insertion order)
print(ep1)        # Output: {122: 67, 657: 59, 351: 78}


# -----------------------------
# del Keyword (Delete Entire Dictionary)
# -----------------------------
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
del ep1           # Deletes the entire dictionary from memory
# print(ep1)      # ❌ This will cause an error: NameError (ep1 no longer exists)


# -----------------------------
# del Keyword (Delete a Specific Key)
# -----------------------------
ep1 = {122: 67, 657: 59, 351: 78, 513: 66}
del ep1[122]      # Deletes the key 122 only
print(ep1)        # Output: {657: 59, 351: 78, 513: 66}
