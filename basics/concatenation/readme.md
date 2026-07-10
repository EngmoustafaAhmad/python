# Python String Concatenation

This lesson explains how to combine strings in Python using different techniques. String concatenation is one of the most common operations when working with text.

## What is String Concatenation?

**Concatenation** means joining two or more strings together to create a single string.

Python uses the **`+`** operator to concatenate strings.

Example:

```python
first_name = "Moustafa"
last_name = " Ahmed"

print(first_name + last_name)
```

**Output**

```text
Moustafa Ahmed
```

---

# Code Explanation

## 1. Basic String Concatenation

```python
first_name = "Moustafa"
last_name = " Ahmed"

print(first_name + last_name)
```

The `+` operator joins the two strings into one.

**Output**

```text
Moustafa Ahmed
```

---

## 2. Concatenating Multiple Strings

```python
language = "Python"
version = "3.13"

print("Learning " + language + " Version " + version)
```

You can concatenate string literals and variables together.

**Output**

```text
Learning Python Version 3.13
```

---

## 3. Line Continuation Using Backslash (`\`)

```python
message = "Welcome to \
Python \
Programming"

print(message)
```

The backslash (`\`) tells Python that the string continues on the next line.

**Output**

```text
Welcome to Python Programming
```

---

## 4. Automatic String Concatenation

```python
letters = (
    "A"
    "B"
    "C"
)

print(letters)
```

Adjacent string literals inside parentheses are automatically combined.

**Output**

```text
ABC
```

---

## 5. Concatenating Variables

```python
city = "Qena"
country = "Egypt"

print(city + ", " + country)
```

You can concatenate variables with additional text.

**Output**

```text
Qena, Egypt
```

---

## 6. String and Integer

```python
number = 20
text = "Age: "

print(text + str(number))
```

A string cannot be concatenated directly with an integer.

Incorrect:

```python
print(text + number)
```

This raises:

```text
TypeError: can only concatenate str (not "int") to str
```

Convert the integer to a string using `str()`.

**Output**

```text
Age: 20
```

---

## 7. Concatenating Different Data Types

```python
name = "Ali"
age = 21
height = 1.75

print("Name: " + name)
print("Age: " + str(age))
print("Height: " + str(height))
```

When concatenating numbers with strings, convert them using `str()`.

**Output**

```text
Name: Ali
Age: 21
Height: 1.75
```

---

## 8. Using f-Strings (Recommended)

```python
print(f"My name is {name}.")
print(f"I am {age} years old.")
```

An **f-string** is the recommended way to insert variables into a string because it is readable and efficient.

**Output**

```text
My name is Ali.
I am 21 years old.
```

---

## 9. Using the `format()` Method

```python
print("My name is {}.".format(name))
print("I am {} years old.".format(age))
```

The `format()` method is another way to insert values into a string.

**Output**

```text
My name is Ali.
I am 21 years old.
```

---

# Comparison

| Method        | Example                   | Recommended |
| ------------- | ------------------------- | ----------- |
| Concatenation | `"Hello " + name`         | ✅ Good      |
| f-String      | `f"Hello {name}"`         | ⭐ Best      |
| `format()`    | `"Hello {}".format(name)` | ✅ Good      |

---

# Best Practices

* Use the `+` operator to join strings.
* Convert numbers to strings using `str()` before concatenation.
* Prefer **f-strings** in modern Python because they are cleaner and easier to read.
* Avoid using `str` as a variable name because it overrides Python's built-in `str()` function.

---

# Files

* `concatenation.py` – Demonstrates different ways to concatenate strings in Python.

---

# Learning Outcome

After completing this lesson, you should be able to:

* Understand string concatenation.
* Join multiple strings using the `+` operator.
* Use line continuation with the backslash (`\`).
* Convert numbers to strings using `str()`.
* Use **f-strings** and the `format()` method for readable string formatting.
