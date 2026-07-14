# ==========================================
# Python Numbers
# ==========================================

# Python has three main numeric data types:
# 1. int
# 2. float
# 3. complex

# ------------------------------------------
# Integer (int)
# ------------------------------------------
print("===== Integer =====")

positive_integer = 10
negative_integer = -10
zero = 0

print(positive_integer)
print(type(positive_integer))

print(negative_integer)
print(type(negative_integer))

print(zero)
print(type(zero))

# ------------------------------------------
# Float (float)
# ------------------------------------------
print("\n===== Float =====")

positive_float = 3.14
negative_float = -3.14

print(positive_float)
print(type(positive_float))

print(negative_float)
print(type(negative_float))

# ------------------------------------------
# Complex (complex)
# ------------------------------------------
print("\n===== Complex =====")

complex_number = 3 + 4j

print(complex_number)
print(type(complex_number))

print("Real Part      :", complex_number.real)
print("Imaginary Part :", complex_number.imag)

# ------------------------------------------
# Type Conversion
# ------------------------------------------
print("\n===== Type Conversion =====")

# Integer to Float
number = 100

print(float(number))

# Integer to Complex
print(complex(number))

# Float to Integer
decimal = 15.99
print(int(decimal))

# Float to Complex
print(complex(decimal))

# ------------------------------------------
# Arithmetic Operations
# ------------------------------------------
print("\n===== Arithmetic =====")

a = 15
b = 4

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Floor Division :", a // b)
print("Modulus        :", a % b)
print("Power          :", a ** b)

# ------------------------------------------
# Absolute Value
# ------------------------------------------
print("\n===== abs() =====")

print(abs(-50))
print(abs(25))

# ------------------------------------------
# Rounding Numbers
# ------------------------------------------
print("\n===== round() =====")

value = 3.14159265

print(round(value))
print(round(value, 2))
print(round(value, 4))

# ------------------------------------------
# Maximum and Minimum
# ------------------------------------------
print("\n===== max() & min() =====")

print(max(5, 10, 20, 15))
print(min(5, 10, 20, 15))

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")