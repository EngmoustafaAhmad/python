# Python Indentation

This lesson demonstrates the importance of **indentation** in Python.

## What is Indentation?

Indentation is the whitespace (usually **4 spaces**) at the beginning of a line of code. Python uses indentation to define code blocks instead of curly braces `{}`.

## Why is Indentation Important?

* Defines the scope of code blocks.
* Makes code more readable.
* Required by Python syntax.

Incorrect indentation will raise an `IndentationError`.

## Example

```python
age = 20

if age >= 18:
    print("Adult")

print("Program finished")
```

### Output

```
Adult
Program finished
```

## Incorrect Example

```python
age = 20

if age >= 18:
print("Adult")
```

Output:

```
IndentationError: expected an indented block
```

## Best Practices

* Use **4 spaces** for each indentation level.
* Do not mix **tabs** and **spaces**.
* Configure your code editor to insert spaces automatically.
* Indent code after statements ending with a colon (`:`), such as:

  * `if`
  * `elif`
  * `else`
  * `for`
  * `while`
  * `def`
  * `class`
  * `try`
  * `except`
  * `with`

## Files

* `indentation.py` – Examples of correct and incorrect indentation.

## Learning Outcome

After completing this lesson, you should be able to:

* Understand why indentation is required in Python.
* Identify common indentation errors.
* Write properly indented Python code.
* Avoid `IndentationError` and `TabError`.
