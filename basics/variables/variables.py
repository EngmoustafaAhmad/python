# ==========================================
# Python Variables
# ==========================================


# source code: original code you write it in your computer
# Translation: Converting source code into machine language
# Compilation: Translate code before runtime
# Runtime: period app take to execute commands
# interpreter: program that executes code line by line

help("keywords")

# ------------------------------------------
# Creating Variables
# ------------------------------------------
name = "Moustafa"
age = 21
height = 1.75
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# ------------------------------------------
# Checking Variable Types
# ------------------------------------------
print("\nVariable Types")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# ------------------------------------------
# Multiple Variable Assignment
# ------------------------------------------
first_name, last_name, country = "Moustafa", "Ahmed", "Egypt"

print("\nMultiple Assignment")
print(first_name)
print(last_name)
print(country)

# ------------------------------------------
# Assign One Value to Multiple Variables
# ------------------------------------------
x = y = z = 100

print("\nOne Value to Multiple Variables")
print("x =", x)
print("y =", y)
print("z =", z)

# ------------------------------------------
# Dynamic Typing
# ------------------------------------------
value = 10
print("\nDynamic Typing")
print(value)
print(type(value))

value = "Python"
print(value)
print(type(value))

value = 3.14
print(value)
print(type(value))

# ------------------------------------------
# Constants (By Convention)
# ------------------------------------------
PI = 3.14159
MAX_USERS = 100

print("\nConstants")
print("PI =", PI)
print("MAX_USERS =", MAX_USERS)

# ------------------------------------------
# Valid Variable Names
# ------------------------------------------
student_name = "Ali"
student_age = 20
_score = 95
score1 = 90

print("\nValid Variable Names")
print(student_name)
print(student_age)
print(_score)
print(score1)

# ------------------------------------------
# Invalid Variable Names (Examples)
# ------------------------------------------

# 1name = "Ali"          # Starts with a number
# student-name = "Sara"  # Hyphen is not allowed
# class = "Python"       # 'class' is a reserved keyword

# ------------------------------------------
# Updating Variables
# ------------------------------------------
counter = 1

print("\nBefore Update:", counter)

counter = counter + 1

print("After Update:", counter)

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")