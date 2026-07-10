# ==========================================
# Python String Concatenation
# ==========================================

# ------------------------------------------
# Basic String Concatenation
# ------------------------------------------
first_name = "Moustafa"
last_name = " Ahmed"

print("1. Basic Concatenation")
print(first_name + last_name)

# ------------------------------------------
# Concatenating Multiple Strings
# ------------------------------------------
language = "Python"
version = "3.13"

print("\n2. Multiple Concatenation")
print("Learning " + language + " Version " + version)

# ------------------------------------------
# Line Continuation Using Backslash
# ------------------------------------------
message = "Welcome to \
Python \
Programming"

print("\n3. Line Continuation")
print(message)

# ------------------------------------------
# Automatic String Concatenation
# ------------------------------------------
letters = (
    "A"
    "B"
    "C"
)

print("\n4. Automatic String Concatenation")
print(letters)

# ------------------------------------------
# Concatenating Variables
# ------------------------------------------
city = "Qena"
country = "Egypt"

print("\n5. Concatenating Variables")
print(city + ", " + country)

# ------------------------------------------
# String and Integer (Incorrect)
# ------------------------------------------
number = 20
text = "Age: "

print("\n6. String + Integer")

# Uncommenting the next line will raise a TypeError
# print(text + number)

# Correct way
print(text + str(number))

# ------------------------------------------
# Concatenating Different Data Types
# ------------------------------------------
name = "Ali"
age = 21
height = 1.75

print("\n7. Different Data Types")
print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height))

# ------------------------------------------
# Using f-Strings (Recommended)
# ------------------------------------------
print("\n8. Using f-Strings")

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My height is {height} meters.")

# ------------------------------------------
# Using format()
# ------------------------------------------
print("\n9. Using format()")

print("My name is {}.".format(name))
print("I am {} years old.".format(age))
print("My height is {} meters.".format(height))

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")