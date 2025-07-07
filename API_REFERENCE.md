# API Reference

This document provides comprehensive documentation for all public APIs, functions, and components in the repo-demo project.

## Table of Contents

- [Module Overview](#module-overview)
- [Functions](#functions)
  - [greet()](#greet)
  - [greet_multiple()](#greet_multiple)
  - [greet_multiple_safe()](#greet_multiple_safe)
- [Classes](#classes)
  - [Greeter](#greeter-class)
- [Constants and Variables](#constants-and-variables)
- [Exceptions](#exceptions)
- [Type Hints](#type-hints)

## Module Overview

The `hello` module provides functionality for generating personalized greeting messages. It includes both functional and object-oriented interfaces for maximum flexibility.

### Module Attributes

- **Author**: Agentic AI Course
- **Version**: 1.0.0
- **License**: [To be specified]

### Dependencies

- Python 3.7+
- typing (built-in)
- logging (built-in)
- collections (built-in, used in Greeter class)

## Functions

### greet()

```python
def greet(name: str, greeting: str = "Hello") -> str
```

Generate a personalized greeting message.

#### Parameters

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `name` | `str` | - | Yes | The name of the person to greet. Must not be empty or whitespace. |
| `greeting` | `str` | `"Hello"` | No | The greeting word to use. |

#### Returns

- **Type**: `str`
- **Description**: A formatted greeting message in the format "{greeting}, {name}!"

#### Raises

- **`ValueError`**: If name is empty or contains only whitespace
- **`TypeError`**: If name or greeting is not a string

#### Examples

```python
# Basic usage
>>> greet("World")
'Hello, World!'

# Custom greeting
>>> greet("Alice", "Hi")
'Hi, Alice!'

# Formal greeting
>>> greet("Dr. Smith", "Good morning")
'Good morning, Dr. Smith!'
```

#### Notes

- The function automatically strips whitespace from names
- Punctuation (!) is automatically added to the end
- Names are case-sensitive
- Empty strings and None values will raise exceptions

---

### greet_multiple()

```python
def greet_multiple(names: List[str], greeting: str = "Hello") -> List[str]
```

Generate greeting messages for multiple people.

#### Parameters

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `names` | `List[str]` | - | Yes | A list of names to greet. Can be empty list. |
| `greeting` | `str` | `"Hello"` | No | The greeting word to use for all names. |

#### Returns

- **Type**: `List[str]`
- **Description**: A list of formatted greeting messages, one for each name

#### Raises

- **`TypeError`**: If names is not a list or greeting is not a string
- **`ValueError`**: If any name in the list is invalid (empty or not a string)

#### Examples

```python
# Multiple people
>>> greet_multiple(["Alice", "Bob", "Charlie"])
['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']

# Custom greeting
>>> greet_multiple(["John", "Jane"], "Hi")
['Hi, John!', 'Hi, Jane!']

# Empty list
>>> greet_multiple([])
[]
```

#### Notes

- All names must be valid strings
- If any name is invalid, the entire function fails
- Use `greet_multiple_safe()` to skip invalid names instead
- Order of output matches order of input

---

### greet_multiple_safe()

```python
def greet_multiple_safe(names: List[str], greeting: str = "Hello") -> List[str]
```

Generate greeting messages for multiple people, skipping invalid names.

#### Parameters

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `names` | `List[str]` | - | Yes | A list of names to greet. Invalid names are skipped. |
| `greeting` | `str` | `"Hello"` | No | The greeting word to use for all valid names. |

#### Returns

- **Type**: `List[str]`
- **Description**: A list of formatted greeting messages for valid names only

#### Raises

- **`TypeError`**: If names is not a list or greeting is not a string

#### Examples

```python
# Mixed valid and invalid names
>>> greet_multiple_safe(["Alice", "", "Bob", None, "Charlie"])
['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']

# All invalid names
>>> greet_multiple_safe(["", " ", None])
[]

# All valid names
>>> greet_multiple_safe(["John", "Jane"])
['Hello, John!', 'Hello, Jane!']
```

#### Notes

- Invalid names are silently skipped
- Warnings are logged for each skipped name
- Empty strings, None values, and non-strings are considered invalid
- More robust than `greet_multiple()` for unreliable input data

---

## Classes

### Greeter Class

```python
class Greeter:
```

A class for managing personalized greetings with customizable settings and history tracking.

#### Constructor

```python
def __init__(self, default_greeting: str = "Hello", case_sensitive: bool = True)
```

##### Parameters

| Parameter | Type | Default | Required | Description |
|-----------|------|---------|----------|-------------|
| `default_greeting` | `str` | `"Hello"` | No | Default greeting to use when none is specified |
| `case_sensitive` | `bool` | `True` | No | Whether to preserve the original case of names |

##### Raises

- **`TypeError`**: If default_greeting is not a string
- **`ValueError`**: If default_greeting is empty

#### Attributes

| Attribute | Type | Description |
|-----------|------|-------------|
| `default_greeting` | `str` | The default greeting used by this instance |
| `case_sensitive` | `bool` | Whether names preserve their original case |
| `greeting_history` | `List[str]` | Complete history of all greetings generated |

#### Methods

##### greet()

```python
def greet(self, name: str, greeting: Optional[str] = None) -> str
```

Generate a greeting message using the class settings.

**Parameters:**
- `name` (str): The name of the person to greet
- `greeting` (str, optional): Custom greeting. Uses default if None

**Returns:** Formatted greeting message

**Raises:** Same exceptions as the module-level `greet()` function

**Example:**
```python
>>> greeter = Greeter("Hi")
>>> greeter.greet("World")
'Hi, World!'
```

##### get_statistics()

```python
def get_statistics(self) -> dict
```

Get statistics about the greetings generated by this instance.

**Returns:** Dictionary with the following keys:
- `total_greetings` (int): Total number of greetings generated
- `unique_names` (int): Number of unique names greeted
- `most_common_greeting` (str): Most frequently used greeting word

**Example:**
```python
>>> greeter = Greeter()
>>> greeter.greet("Alice")
>>> greeter.greet("Bob")
>>> stats = greeter.get_statistics()
>>> print(stats)
{'total_greetings': 2, 'unique_names': 2, 'most_common_greeting': 'Hello'}
```

##### clear_history()

```python
def clear_history(self) -> None
```

Clear the greeting history while preserving configuration settings.

**Example:**
```python
>>> greeter.clear_history()
>>> len(greeter.greeting_history)
0
```

#### Usage Examples

```python
# Basic usage
greeter = Greeter()
message = greeter.greet("World")

# Custom default greeting
greeter = Greeter("Good morning")
message = greeter.greet("Alice")

# Case insensitive mode
greeter = Greeter(case_sensitive=False)
message = greeter.greet("john doe")  # Will be converted to "John Doe"

# Tracking statistics
greeter = Greeter()
greeter.greet("Alice")
greeter.greet("Bob", "Hi")
stats = greeter.get_statistics()
```

## Constants and Variables

### Module-level Variables

- **`logger`**: logging.Logger instance for the hello module
- **`__version__`**: Module version string (implicitly "1.0.0")

## Exceptions

### Built-in Exceptions Used

- **`ValueError`**: Raised when parameters have correct type but invalid values
- **`TypeError`**: Raised when parameters have incorrect types

### Exception Handling Examples

```python
try:
    result = greet("")  # Empty name
except ValueError as e:
    print(f"Invalid name: {e}")

try:
    result = greet(123)  # Wrong type
except TypeError as e:
    print(f"Type error: {e}")
```

## Type Hints

The module uses comprehensive type hints for better IDE support and code clarity:

```python
from typing import List, Optional, Union
```

### Common Type Patterns

- `str`: String parameters and return values
- `List[str]`: Lists of strings (e.g., names)
- `Optional[str]`: String parameters that can be None
- `bool`: Boolean configuration flags
- `dict`: Dictionary return values (statistics)

## Performance Considerations

- **Function calls**: All functions have O(1) complexity for single operations
- **Multiple greetings**: O(n) where n is the number of names
- **History tracking**: Greeter class maintains full history in memory
- **Memory usage**: Each greeting message stored as string in history

## Thread Safety

- Module-level functions are thread-safe (no shared state)
- Greeter instances are **not** thread-safe due to shared history
- For concurrent usage, create separate Greeter instances per thread

## Version Compatibility

- **Minimum Python version**: 3.7+
- **Type hints**: Requires Python 3.5+ for basic support, 3.7+ for full support
- **Dependencies**: Uses only standard library modules