# Python Arithmetic Operators

This lesson introduces Python's arithmetic operators, which are used to perform mathematical calculations on numeric values.

## What are Arithmetic Operators?

Arithmetic operators allow you to perform basic mathematical operations such as addition, subtraction, multiplication, division, and more.

Python supports the following arithmetic operators:

| Operator | Name           | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `5 + 3`  |
| `-`      | Subtraction    | `5 - 3`  |
| `*`      | Multiplication | `5 * 3`  |
| `/`      | Division       | `5 / 3`  |
| `%`      | Modulus        | `5 % 3`  |
| `**`     | Exponentiation | `5 ** 3` |
| `//`     | Floor Division | `5 // 3` |

---

# Code Explanation

## 1. Creating Variables

```python
a = 20
b = 6
```

These variables will be used in all arithmetic operations.

---

## 2. Addition (`+`)

```python
result = a + b
print(result)
```

The `+` operator adds two numbers.

**Output**

```text
26
```

---

## 3. Subtraction (`-`)

```python
result = a - b
print(result)
```

The `-` operator subtracts the second number from the first.

**Output**

```text
14
```

---

## 4. Multiplication (`*`)

```python
result = a * b
print(result)
```

The `*` operator multiplies two numbers.

**Output**

```text
120
```

---

## 5. Division (`/`)

```python
result = a / b
print(result)
```

The `/` operator always returns a floating-point value.

**Output**

```text
3.3333333333333335
```

---

## 6. Modulus (`%`)

```python
result = a % b
print(result)
```

The modulus operator returns the remainder after division.

Example:

```
20 ÷ 6 = 3 remainder 2
```

**Output**

```text
2
```

---

## 7. Exponentiation (`**`)

```python
result = a ** b
print(result)
```

Raises the first number to the power of the second.

Example:

```
20⁶
```

**Output**

```text
64000000
```

---

## 8. Floor Division (`//`)

```python
result = a // b
print(result)
```

Floor division returns the integer part of the division result by discarding the decimal portion.

Example:

```
20 / 6 = 3.333...
20 // 6 = 3
```

**Output**

```text
3
```

---

## 9. Arithmetic with Floating-Point Numbers

```python
x = 10.5
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)
```

Arithmetic operators also work with floating-point numbers.

---

# Operator Summary

| Operator | Description    | Example   |     Result |
| -------- | -------------- | --------- | ---------: |
| `+`      | Addition       | `20 + 6`  |       `26` |
| `-`      | Subtraction    | `20 - 6`  |       `14` |
| `*`      | Multiplication | `20 * 6`  |      `120` |
| `/`      | Division       | `20 / 6`  | `3.333...` |
| `%`      | Modulus        | `20 % 6`  |        `2` |
| `**`     | Exponentiation | `20 ** 6` | `64000000` |
| `//`     | Floor Division | `20 // 6` |        `3` |

---

# Difference Between `/` and `//`

```python
print(20 / 6)
print(20 // 6)
```

Output:

```text
3.3333333333333335
3
```

* `/` returns the exact division result as a **float**.
* `//` returns the floor (rounded down) result.

---

# Operator Precedence

Python evaluates arithmetic expressions according to precedence rules:

1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
4. Addition `+`, Subtraction `-`

Example:

```python
result = 5 + 2 * 3
print(result)
```

Output:

```text
11
```

because multiplication is evaluated before addition.

---

# Best Practices

* Use descriptive variable names such as `price`, `total`, or `quantity`.
* Use parentheses to make complex expressions easier to read.
* Use `/` when you need the exact decimal result.
* Use `//` when you only need the whole-number quotient.
* Use `%` to determine whether a number is even or odd.

Example:

```python
number = 8

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# Files

* `arithmetic_operators.py` — Demonstrates all arithmetic operators with integers and floating-point numbers.

---

# Learning Outcome

After completing this lesson, you should be able to:

* Perform addition, subtraction, multiplication, and division.
* Understand the difference between `/` and `//`.
* Calculate remainders using the modulus operator.
* Raise numbers to powers using `**`.
* Apply arithmetic operators to both integers and floating-point numbers.
* Write and evaluate arithmetic expressions confidently.
