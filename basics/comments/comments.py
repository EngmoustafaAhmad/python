# ==========================================
# Python Comments
# ==========================================

# This is a single-line comment.
print("Welcome to Python!")

# Variables
name = "Moustafa"  # Store the user's name
age = 21           # Store the user's age

# Display the variables
print("Name:", name)
print("Age:", age)

# ------------------------------------------
# Multi-line comments
# ------------------------------------------

# Python does not have a true multi-line comment.
# We usually write multiple single-line comments
# to explain a block of code.

# ------------------------------------------
# Triple-quoted strings
# ------------------------------------------

"""
This is a multi-line string.

Although developers sometimes use triple quotes
as comments, they are actually string literals.
"""

# ------------------------------------------
# Using comments to explain logic
# ------------------------------------------

# Check if the user is an adult
if age >= 18:
    print(name, "is an adult.")
else:
    print(name, "is a minor.")

# ------------------------------------------
# Temporarily disabling code
# ------------------------------------------

# Uncomment the lines below to test them.

# print("This line is currently disabled.")
# print("So is this one.")

# ------------------------------------------
# End of program
# ------------------------------------------

print("Program finished.")