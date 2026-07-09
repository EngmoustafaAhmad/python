# Python Escape Sequences

This lesson introduces **escape sequences** in Python. Escape sequences are special character combinations that begin with a backslash (`\`) and represent characters that cannot be typed directly or have special meanings.

## What are Escape Sequences?

An escape sequence starts with a backslash (`\`) followed by one or more characters.

Example:

```python
print("Hello\nPython")
```

Output:

```text
Hello
Python
```

## Common Escape Sequences

| Escape Sequence | Description                            |
| --------------- | -------------------------------------- |
| `\\`            | Backslash (`\`)                        |
| `\'`            | Single quote                           |
| `\"`            | Double quote                           |
| `\n`            | New line                               |
| `\t`            | Horizontal tab                         |
| `\r`            | Carriage return                        |
| `\b`            | Backspace                              |
| `\f`            | Form feed                              |
| `\v`            | Vertical tab                           |
| `\a`            | ASCII bell (may produce a beep)        |
| `\ooo`          | Character with an octal value          |
| `\xhh`          | Character with a hexadecimal value     |
| `\uhhhh`        | Unicode character (16-bit hexadecimal) |
| `\Uhhhhhhhh`    | Unicode character (32-bit hexadecimal) |
| `\N{name}`      | Unicode character by its official name |

## Examples

### New Line

```python
print("Hello\nPython")
```

Output:

```text
Hello
Python
```

### Horizontal Tab

```python
print("Name\tAge")
```

Output:

```text
Name    Age
```

### Backslash

```python
print("C:\\Users\\Moustafa")
```

Output:

```text
C:\Users\Moustafa
```

### Unicode

```python
print("\u03A9")
```

Output:

```text
Ω
```

### Emoji

```python
print("\U0001F600")
```

Output:

```text
😀
```

## Invalid Escape Sequences

The following are **not valid Python escape sequences**:

* `\c`
* `\e`

Using them may produce warnings or errors depending on your Python version.

## Best Practices

* Use raw strings (`r"..."`) when working with Windows file paths or regular expressions.
* Use `\n` to improve output formatting.
* Use `\t` to align text in the console.
* Prefer Unicode escape sequences when representing special symbols programmatically.

## Files

* `escape_sequences.py` — Demonstrates the most common Python escape sequences.

## Learning Outcome

After completing this lesson, you should be able to:

* Understand what escape sequences are.
* Use common escape sequences in strings.
* Display Unicode characters and emojis.
* Distinguish between valid and invalid Python escape sequences.
