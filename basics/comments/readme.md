# Python Comments

This lesson explains how to use comments in Python to make your code easier to understand and maintain.

## What are Comments?

Comments are lines of text that Python ignores when executing a program. They are used to explain code, leave notes, or temporarily disable code during testing.

## Single-Line Comments

Use the `#` symbol to create a single-line comment.

```python
# This is a single-line comment
print("Hello, World!")
```

You can also place a comment at the end of a line of code.

```python
x = 10  # Store the value 10 in x
```

## Multi-Line Comments

Python does not have a dedicated multi-line comment syntax. The common approach is to use multiple single-line comments.

```python
# This program calculates
# the sum of two numbers
# and displays the result.
```

You may also see triple quotes (`'''` or `"""``) used for multi-line text.

```python
"""
This is a multi-line string.
It is often used as a comment,
but it is actually a string object.
"""
```

## Why Use Comments?

* Explain complex code.
* Improve code readability.
* Make maintenance easier.
* Help other developers understand your code.
* Temporarily disable code while debugging.

## Best Practices

* Write clear and meaningful comments.
* Explain **why** the code exists, not just **what** it does.
* Keep comments up to date when the code changes.
* Avoid unnecessary comments for obvious code.

## Example

```python
# Ask the user for their name
name = input("Enter your name: ")

# Display a greeting
print(f"Hello, {name}!")
```

## Files

* `comments.py` – Examples of single-line and multi-line comments.

## Learning Outcome

After completing this lesson, you should be able to:

* Write single-line comments using `#`.
* Understand how multi-line comments are typically written.
* Use comments to improve code readability.
* Follow comment best practices in Python.
