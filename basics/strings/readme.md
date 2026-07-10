# Python Strings

This lesson introduces **strings** in Python and demonstrates how to create, display, and manipulate text.

## What is a String?

A **string** is a sequence of characters used to represent text. In Python, strings are immutable, which means their contents cannot be changed after they are created.

Strings can be created using:

* Single quotes (`'...'`)
* Double quotes (`"..."`)
* Triple quotes (`'''...'''` or `"""..."""`)

---

# Code Explanation

## 1. Single-Quoted String

```python
myStringOne = 'This is Single Quote'
print(myStringOne)
```

This creates a string using **single quotes**.

**Output**

```text
This is Single Quote
```

---

## 2. Double-Quoted String

```python
myStringTwo = "This is Double Quotes"
print(myStringTwo)
```

This creates a string using **double quotes**.

**Output**

```text
This is Double Quotes
```

---

## 3. Double Quotes Inside a String

```python
myStringThree = 'This is Single Quote "Test"'
print(myStringThree)
```

Since the string is enclosed in **single quotes**, double quotes can be used inside without escaping them.

**Output**

```text
This is Single Quote "Test"
```

---

## 4. Single Quotes Inside a String

```python
myStringFour = "This is Double Quotes 'Test'"
print(myStringFour)
```

Since the string is enclosed in **double quotes**, single quotes can appear inside without escaping them.

**Output**

```text
This is Double Quotes 'Test'
```

---

## 5. Triple-Quoted (Multi-line) Strings

```python
myStr = """
Hello everybody
Who are you?
How are you?
"""

print(myStr)
```

Triple quotes allow a string to span multiple lines while preserving the formatting.

**Output**

```text
Hello everybody
Who are you?
How are you?
```

---

## 6. Using Backslashes

```python
myStr = """
hello everybody who \\are you and \\
how are you
"""

print(myStr)
```

### Explanation

* `\\` displays a single backslash (`\`).
* A backslash (`\`) at the end of a line escapes the newline, so the next line is treated as a continuation of the current one.

---

## 7. String Concatenation

```python
first = "Hello"
second = " Python"

print(first + second)
```

The `+` operator joins two strings together.

**Output**

```text
Hello Python
```

---

## 8. String Repetition

```python
print("Python! " * 3)
```

The `*` operator repeats a string a specified number of times.

**Output**

```text
Python! Python! Python!
```

---

## 9. Finding the Length of a String

```python
language = "Python"

print(len(language))
```

The `len()` function returns the number of characters in a string.

**Output**

```text
6
```

---

## 10. Accessing Characters (Indexing)

```python
language = "Python"

print(language[0])
print(language[-1])
```

Strings are indexed starting from **0**.

* `0` → First character
* `-1` → Last character

**Output**

```text
P
n
```

---

# Single Quotes vs Double Quotes

Both of the following are equivalent:

```python
text1 = 'Python'
text2 = "Python"
```

Choose the style that makes your code easier to read. For example, use double quotes if the string contains a single quote:

```python
message = "It's a beautiful day."
```

or use single quotes if the string contains double quotes:

```python
message = 'He said "Hello!"'
```

---

# Best Practices

* Use meaningful variable names such as `message`, `text`, or `name`.
* Use triple quotes for multi-line text.
* Choose the quote style that minimizes escaping.
* Use `len()` to determine the length of a string.
* Remember that strings are **immutable**, so you cannot modify individual characters directly.

---

# Files

* `strings.py` — Demonstrates different ways to create strings, use quotes, create multi-line strings, work with escape characters, concatenate strings, repeat strings, and access individual characters.

---

# Learning Outcome

After completing this lesson, you should be able to:

* Create strings using single, double, and triple quotes.
* Include quotes inside strings correctly.
* Understand escape characters and backslashes.
* Concatenate and repeat strings.
* Find the length of a string.
* Access individual characters using indexing.
* Understand that Python strings are immutable.
