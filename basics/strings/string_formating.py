# ==========================================
# Python String Formatting
# ==========================================

# ------------------------------------------
# Variables
# ------------------------------------------
name = "Moustafa"
age = 21
rank = 1
degree = 22.2424

# ------------------------------------------
# String Concatenation
# ------------------------------------------
print("===== String Concatenation =====")

# Incorrect:
# print("My name is " + name + " and I am " + age + " years old")
# TypeError: Cannot concatenate a string with an integer.

print("My name is " + name + " and I am " + str(age) + " years old")

# ------------------------------------------
# f-Strings (Recommended)
# ------------------------------------------
print("\n===== f-Strings =====")

print(f"My name is {name} and I am {age} years old.")
print(f"My rank is {rank}.")
print(f"My degree is {degree:.2f}.")

# ------------------------------------------
# Old Style Formatting (% Operator)
# ------------------------------------------
print("\n===== % Formatting =====")

print("My name is %s" % name)
print("My name is %s and I am %d years old." % (name, age))
print("My name is %s and I am %d years old. My rank is %d." % (name, age, rank))

# ------------------------------------------
# Formatting Numbers
# ------------------------------------------
print("\n===== Number Formatting =====")

number = 10

print("%d" % number)
print("%f" % number)
print("%.2f" % number)

# ------------------------------------------
# Formatting Strings
# ------------------------------------------
print("\n===== String Precision =====")

message = "Hello people, how are you?"

print("%s" % message)
print("%.5s" % message)

# ------------------------------------------
# format() Method
# ------------------------------------------
print("\n===== format() Method =====")

print(
    "My name is {:s}, I am {:d} years old, and my degree is {:.2f}"
    .format(name, age, degree)
)

# ------------------------------------------
# Thousand Separator
# ------------------------------------------
print("\n===== Thousand Separator =====")

money = 12323123232323234

print("My money is {:,}".format(money))

# ------------------------------------------
# Positional Formatting (Strings)
# ------------------------------------------
print("\n===== Positional Formatting =====")

first = "One"
second = "Two"
third = "Three"

print("{} {} {}".format(first, second, third))
print("{2} {1} {0}".format(first, second, third))

# ------------------------------------------
# Positional Formatting (Numbers)
# ------------------------------------------
print("\n===== Positional Numbers =====")

x, y, z = 1, 2, 3

print("{} {} {}".format(x, y, z))
print("{2} {1} {0}".format(x, y, z))
print("{1:d} {2:d} {0:d}".format(z, y, x))

# ------------------------------------------
# Named Arguments
# ------------------------------------------
print("\n===== Named Arguments =====")

print(
    "Name: {name}, Age: {age}, Rank: {rank}"
    .format(name=name, age=age, rank=rank)
)

# ------------------------------------------
# Alignment
# ------------------------------------------
print("\n===== Alignment =====")

print("{:<15}".format("Left"))
print("{:^15}".format("Center"))
print("{:>15}".format("Right"))

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")