# String formatting using format() with positional indexes
# {0} -> first argument, {1} -> second argument
letter = "Hello my name is {1} and I'm from {0}"
country = "Pakistan"
name = "Shahnam"

# Here country = Pakistan goes to {0}, and name = Shahnam goes to {1}
print(letter.format(country, name))   # Output: Hello my name is Shahnam and I'm from Pakistan

# f-string method (more modern and easier)
print(f"Hello my name is {name} and I'm from {country}")

# Formatting numbers: {:.2f} means "2 decimal places float"
txt = "For only {price:.2f} dollars"
print(txt.format(price = 49.0999))   # Output: For only 49.10 dollars

# f-strings also allow direct expressions (calculations inside {})
print(f"{2 * 30}")   # Output: 60
