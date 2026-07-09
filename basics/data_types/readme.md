# Python Data Types

This lesson introduces Python's built-in data types and demonstrates how they are used to store different kinds of values.

## What Are Data Types?

A **data type** defines the type of value a variable can hold. Python automatically determines a variable's data type based on the value assigned to it.

## Built-in Data Types

### Numeric Types

| Data Type | Description     | Example         |
| --------- | --------------- | --------------- |
| `int`     | Integer numbers | `10`, `-5`      |
| `float`   | Decimal numbers | `3.14`, `19.99` |
| `complex` | Complex numbers | `2 + 3j`        |

### Boolean Type

| Data Type | Description    | Example         |
| --------- | -------------- | --------------- |
| `bool`    | Logical values | `True`, `False` |

### Text Type

| Data Type | Description            | Example   |
| --------- | ---------------------- | --------- |
| `str`     | Sequence of characters | `"Hello"` |

### Sequence Types

| Data Type | Description                   | Example     |
| --------- | ----------------------------- | ----------- |
| `list`    | Ordered, mutable collection   | `[1, 2, 3]` |
| `tuple`   | Ordered, immutable collection | `(1, 2, 3)` |
| `range`   | Sequence of numbers           | `range(5)`  |

### Mapping Type

| Data Type | Description     | Example           |
| --------- | --------------- | ----------------- |
| `dict`    | Key-value pairs | `{"name": "Ali"}` |

### Set Types

| Data Type   | Description                           | Example                |
| ----------- | ------------------------------------- | ---------------------- |
| `set`       | Unordered collection of unique values | `{1, 2, 3}`            |
| `frozenset` | Immutable set                         | `frozenset({1, 2, 3})` |

### Binary Types

| Data Type    | Description                | Example                |
| ------------ | -------------------------- | ---------------------- |
| `bytes`      | Immutable binary data      | `b"Hello"`             |
| `bytearray`  | Mutable binary data        | `bytearray(5)`         |
| `memoryview` | Memory view of binary data | `memoryview(bytes(5))` |

### None Type

| Data Type  | Description                       | Example |
| ---------- | --------------------------------- | ------- |
| `NoneType` | Represents the absence of a value | `None`  |

## Checking a Variable's Type

Use the built-in `type()` function to determine a variable's data type.

```python
x = 10
print(type(x))

name = "Python"
print(type(name))

numbers = [1, 2, 3]
print(type(numbers))
```

## Mutable vs Immutable

### Mutable Data Types

These data types can be modified after creation.

* `list`
* `dict`
* `set`
* `bytearray`

### Immutable Data Types

These data types cannot be modified after creation.

* `int`
* `float`
* `complex`
* `bool`
* `str`
* `tuple`
* `bytes`
* `frozenset`

## Best Practices

* Use meaningful variable names.
* Choose the appropriate data type for your data.
* Use `type()` while learning to verify data types.
* Use lists when data needs to change.
* Use tuples for fixed collections of values.
* Use dictionaries to store related information as key-value pairs.

## Files

* `data_types.py` — Demonstrates Python's most commonly used data types with practical examples.

## Learning Outcome

After completing this lesson, you should be able to:

* Understand Python's built-in data types.
* Create variables using different data types.
* Check a variable's type using `type()`.
* Distinguish between mutable and immutable data types.
* Select the appropriate data type for different programming tasks.
