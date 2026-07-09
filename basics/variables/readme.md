# Python Variables

This lesson introduces variables in Python and explains how they are used to store and manage data.

## What is a Variable?

A **variable** is a named location in memory that stores a value. You can think of it as a container that holds data, which can be used and modified throughout your program.

Python creates a variable automatically when you assign a value to it.

## Creating Variables

Assign a value to a variable using the assignment operator (`=`).

```python
name = "Moustafa"
age = 21
height = 1.75
```

## Variable Naming Rules

A variable name:

* Must start with a letter (`a-z`, `A-Z`) or an underscore (`_`).
* Cannot start with a number.
* Can contain letters, numbers, and underscores.
* Is case-sensitive (`age`, `Age`, and `AGE` are different variables).
* Cannot be a Python keyword.

### Valid Variable Names

```python
name = "Ali"
_age = 20
student_name = "Sara"
score1 = 95
```

### Invalid Variable Names

```python
1name = "Ali"       # Starts with a number
student-name = "Sara"  # Hyphen is not allowed
class = "Python"    # Reserved keyword
```

## Multiple Variable Assignment

Assign multiple values in one line.

```python
name, age, country = "Ali", 20, "Egypt"
```

Assign the same value to multiple variables.

```python
x = y = z = 100
```

## Dynamic Typing

Python is a dynamically typed language, meaning a variable's type is determined automatically and can change.

```python
value = 10
print(type(value))

value = "Python"
print(type(value))
```

## Constants

Python does not have true constants. By convention, variables that should not change are written in uppercase.

```python
PI = 3.14159
MAX_USERS = 100
```

## Best Practices

* Use meaningful and descriptive variable names.
* Follow the `snake_case` naming convention.

```python
first_name = "Ali"
student_age = 20
total_score = 95
```

* Avoid single-letter variable names unless used in loops.
* Use uppercase names for constants.

## Files

* `variables.py` — Demonstrates variable declaration, assignment, naming conventions, and dynamic typing.

## Learning Outcome

After completing this lesson, you should be able to:

* Create and use variables.
* Follow Python's variable naming rules.
* Assign values to multiple variables.
* Understand dynamic typing.
* Write clean and readable variable names using `snake_case`.
