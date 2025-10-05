# -----------------------------
# Example 1: for loop with else
# -----------------------------
# The else block runs after the loop finishes normally (without a break)
for i in range(5):
    print(i)            # Prints numbers 0 to 4
else:
    print("Sorry no i") # Runs after the loop completes successfully


# -----------------------------
# Example 2: Empty loop with else
# -----------------------------
# If the loop body never executes, the else block still runs
for i in []:
    print(i) 
else:
    print("Sorry no i") # Will execute because the loop never ran


# -----------------------------
# Example 3: for loop with break
# -----------------------------
# The else block does NOT run if the loop is terminated by 'break'
for i in range(6):
    print(i)
    if i == 4:
        break            # Loop stops when i equals 4
else:
    print("Sorry no i")  # ❌ This will NOT run because of the break


# -----------------------------
# Example 4: while loop with else
# -----------------------------
# 'else' in a while loop also runs only if the loop ends normally
i = 0
while i < 7:
    print(i)
    i = i + 1
    if i == 4:
        break            # Break prevents the else block from running
else:
    print("Sorry no i")  # ❌ Skipped due to break


# -----------------------------
# Example 5: for-else final demonstration
# -----------------------------
for x in range(5):
    print("Iteration no {} in for loop".format(x + 1))
else:
    print("Else block in loop")  # Executes when loop completes all iterations

print("Out of loop")             # Runs after the loop and else block
