# Python Numbers

This lesson introduces Python's numeric data types, type conversion, and common operations.

## What are Numbers in Python?

Python provides three built-in numeric data types:

* `int` – Integer numbers
* `float` – Decimal numbers
* `complex` – Complex numbers

Python automatically determines the appropriate numeric type when you assign a value.

---

# Numeric Data Types

| Data Type | Description                            | Example         |
| --------- | -------------------------------------- | --------------- |
| `int`     | Whole numbers                          | `10`, `-5`, `0` |
| `float`   | Decimal numbers                        | `3.14`, `-2.5`  |
| `complex` | Numbers with a real and imaginary part | `3 + 4j`        |

---

# Code Explanation

## 1. Integer (`int`)

```python
positive_integer = 10
negative_integer = -10
zero = 0

print(type(positive_integer))
```

Integers represent whole numbers without decimal points.

**Output**

```text
<class 'int'>
```

---

## 2. Float (`float`)

```python
positive_float = 3.14
negative_float = -3.14

print(type(positive_float))
```

Floats represent numbers with decimal points.

**Output**

```text
<class 'float'>
```

---

## 3. Complex Numbers (`complex`)

```python
complex_number = 3 + 4j

print(type(complex_number))
```

Complex numbers consist of:

* **Real part**
* **Imaginary part**

You can access them using:

```python
print(complex_number.real)
print(complex_number.imag)
```

**Output**

```text
3.0
4.0
```

---

## 4. Type Conversion

Python allows converting between numeric types.

### Integer to Float

```python
number = 100

print(float(number))
```

Output

```text
100.0
```

### Integer to Complex

```python
print(complex(number))
```

Output

```text
(100+0j)
```

### Float to Integer

```python
decimal = 15.99

print(int(decimal))
```

Output

```text
15
```

> **Note:** Converting a float to an integer removes the decimal part; it does **not** round the value.

### Float to Complex

```python
print(complex(decimal))
```

Output

```text
(15.99+0j)
```

---

## 5. Arithmetic Operations

Python supports the standard arithmetic operators.

```python
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

| Operator | Description            |
| -------- | ---------------------- |
| `+`      | Addition               |
| `-`      | Subtraction            |
| `*`      | Multiplication         |
| `/`      | Division               |
| `//`     | Floor Division         |
| `%`      | Modulus (Remainder)    |
| `**`     | Exponentiation (Power) |

---

## 6. Absolute Value

```python
print(abs(-50))
```

The `abs()` function returns the absolute (positive) value of a number.

**Output**

```text
50
```

---

## 7. Rounding Numbers

```python
value = 3.14159265

print(round(value))
print(round(value, 2))
```

The `round()` function rounds a number to the specified number of decimal places.

**Output**

```text
3
3.14
```

---

## 8. Maximum and Minimum

```python
print(max(5, 10, 20, 15))
print(min(5, 10, 20, 15))
```

* `max()` returns the largest value.
* `min()` returns the smallest value.

**Output**

```text
20
5
```

---

# Type Conversion Summary

| Function    | Description                          |
| ----------- | ------------------------------------ |
| `int()`     | Converts a value to an integer       |
| `float()`   | Converts a value to a float          |
| `complex()` | Converts a value to a complex number |

---

# Best Practices

* Use `int` for whole numbers.
* Use `float` for values containing decimals.
* Use `complex` when working with mathematical or engineering calculations involving imaginary numbers.
* Use `type()` while learning to verify a variable's data type.
* Be aware that converting a float to an integer truncates the decimal part.

---

# Files

* `numbers.py` — Demonstrates Python numeric data types, type conversion, arithmetic operations, and useful numeric functions.

---

# Learning Outcome

After completing this lesson, you should be able to:

* Understand Python's numeric data types.
* Create and use integers, floats, and complex numbers.
* Access the real and imaginary parts of a complex number.
* Convert between numeric types.
* Perform arithmetic operations.
* Use built-in numeric functions such as `abs()`, `round()`, `max()`, and `min()`.
