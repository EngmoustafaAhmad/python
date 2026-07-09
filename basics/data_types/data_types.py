# ==========================================
# Python Data Types
# ==========================================

# ------------------------------------------
# Integer (int)
# ------------------------------------------
age = 21
print("Integer:", age)
print("Type:", type(age))

# ------------------------------------------
# Float (float)
# ------------------------------------------
height = 1.75
print("\nFloat:", height)
print("Type:", type(height))

# ------------------------------------------
# Complex (complex)
# ------------------------------------------
complex_number = 3 + 4j
print("\nComplex:", complex_number)
print("Type:", type(complex_number))

# ------------------------------------------
# Boolean (bool)
# ------------------------------------------
is_student = True
print("\nBoolean:", is_student)
print("Type:", type(is_student))

# ------------------------------------------
# String (str)
# ------------------------------------------
name = "Moustafa"
print("\nString:", name)
print("Type:", type(name))

# ------------------------------------------
# List (list)
# ------------------------------------------
fruits = ["Apple", "Banana", "Orange"]

print("\nList:", fruits)
print("Type:", type(fruits))

# Lists are mutable
fruits.append("Mango")
print("Updated List:", fruits)

# ------------------------------------------
# Tuple (tuple)
# ------------------------------------------
coordinates = (10, 20)

print("\nTuple:", coordinates)
print("Type:", type(coordinates))

# ------------------------------------------
# Set (set)
# ------------------------------------------
numbers = {1, 2, 3, 2, 1}

print("\nSet:", numbers)
print("Type:", type(numbers))

# ------------------------------------------
# Dictionary (dict)
# ------------------------------------------
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}

print("\nDictionary:", student)
print("Type:", type(student))
print("Student Name:", student["name"])

# ------------------------------------------
# NoneType
# ------------------------------------------
result = None

print("\nNone:", result)
print("Type:", type(result))

# ------------------------------------------
# Checking Variable Types
# ------------------------------------------
print("\nChecking Data Types")
print(type(age))
print(type(height))
print(type(name))
print(type(fruits))
print(type(student))