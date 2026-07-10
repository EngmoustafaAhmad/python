# ==========================================
# Python String Indexing & Slicing
# ==========================================

# ------------------------------------------
# Creating a String
# ------------------------------------------
my_string = "Python"

print("String:", my_string)

# ------------------------------------------
# Positive Indexing
# ------------------------------------------
print("\nPositive Indexing")

print("First Character :", my_string[0])
print("Second Character:", my_string[1])
print("Third Character :", my_string[2])
print("Fourth Character:", my_string[3])
print("Fifth Character :", my_string[4])
print("Sixth Character :", my_string[5])

# ------------------------------------------
# Negative Indexing
# ------------------------------------------
print("\nNegative Indexing")

print("Last Character        :", my_string[-1])
print("Second Last Character :", my_string[-2])
print("Third Last Character  :", my_string[-3])

# ------------------------------------------
# Basic Slicing
# ------------------------------------------
print("\nBasic Slicing")

print("Characters 0 to 2 :", my_string[0:3])
print("Characters 3 to 5 :", my_string[3:6])
print("First 4 Characters:", my_string[:4])
print("From Index 2      :", my_string[2:])
print("Entire String     :", my_string[:])

# ------------------------------------------
# Slicing with Step
# ------------------------------------------
print("\nSlicing with Step")

print("Every Character   :", my_string[::1])
print("Every 2nd Character:", my_string[::2])
print("Every 3rd Character:", my_string[::3])

# ------------------------------------------
# Reverse a String
# ------------------------------------------
print("\nReverse String")

print(my_string[::-1])

# ------------------------------------------
# Reverse with Step
# ------------------------------------------
print("\nReverse Every 2nd Character")

print(my_string[::-2])

# ------------------------------------------
# String Length
# ------------------------------------------
print("\nString Length")

print(len(my_string))

# ------------------------------------------
# Indexing Another String
# ------------------------------------------
language = "Programming"

print("\nAnother Example")

print("First Character :", language[0])
print("Last Character  :", language[-1])
print("First 7 Letters :", language[:7])
print("Last 4 Letters  :", language[-4:])
print("Every 2nd Letter:", language[::2])

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")