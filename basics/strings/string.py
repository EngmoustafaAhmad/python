# ==========================================
# Python Strings
# ==========================================

# ------------------------------------------
# Single and Double Quotes
# ------------------------------------------
my_string_one = 'This is Single Quote'
my_string_two = "This is Double Quote"

print("1. Single and Double Quotes")
print(my_string_one)
print(my_string_two)

# ------------------------------------------
# Quotes Inside Strings
# ------------------------------------------
my_string_three = 'This is Single Quote "Test"'
my_string_four = "This is Double Quote 'Test'"

print("\n2. Quotes Inside Strings")
print(my_string_three)
print(my_string_four)

# ------------------------------------------
# Multi-Line String
# ------------------------------------------
my_string_five = """
Hello Everybody
Who Are You?
How Are You?
"""

print("\n3. Multi-Line String")
print(my_string_five)

# ------------------------------------------
# Backslash in Strings
# ------------------------------------------
my_string_six = """
Hello Everybody \\ Who Are You?
This line contains a backslash.
"""

print("4. Backslash in Strings")
print(my_string_six)

# ------------------------------------------
# String Concatenation
# ------------------------------------------
first_name = "Moustafa"
last_name = " Ahmed"

print("5. String Concatenation")
print(first_name + last_name)

# ------------------------------------------
# String Repetition
# ------------------------------------------
print("\n6. String Repetition")
print("Python " * 3)

# ------------------------------------------
# String Length
# ------------------------------------------
language = "Python"

print("\n7. String Length")
print("Length:", len(language))

# ------------------------------------------
# Accessing Characters
# ------------------------------------------
print("\n8. Accessing Characters")
print("First Character:", language[0])
print("Last Character:", language[-1])

# ------------------------------------------
# String Slicing
# ------------------------------------------
print("\n9. String Slicing")
print(language[0:3])   # Pyt
print(language[2:])    # thon
print(language[:4])    # Pyth

# ------------------------------------------
# String Methods
# ------------------------------------------
message = "hello python"

print("\n10. String Methods")
print(message.upper())
print(message.capitalize())
print(message.title())

# ------------------------------------------
# Checking Substrings
# ------------------------------------------
print("\n11. Membership Operators")

print("python" in message)
print("java" in message)

# ------------------------------------------
# Escape Sequences
# ------------------------------------------
print("\n12. Escape Sequences")

print("Hello\nPython")
print("Name\tAge")
print("It's a beautiful day.")
print("C:\\Users\\Moustafa")

# ------------------------------------------
# f-Strings
# ------------------------------------------
name = "Ali"
age = 21

print("\n13. f-Strings")
print(f"My name is {name} and I am {age} years old.")

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")