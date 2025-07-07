# Examples and Tutorials

This document provides comprehensive examples and tutorials for using the repo-demo hello module. Each example includes explanations, code snippets, and expected outputs.

## Table of Contents

- [Basic Usage](#basic-usage)
- [Function Examples](#function-examples)
- [Class Examples](#class-examples)
- [Error Handling](#error-handling)
- [Advanced Use Cases](#advanced-use-cases)
- [Integration Examples](#integration-examples)
- [Performance Tips](#performance-tips)

## Basic Usage

### Quick Start

The simplest way to use the hello module:

```python
from hello import greet

# Generate a basic greeting
message = greet("World")
print(message)
# Output: Hello, World!
```

### Import Options

```python
# Import specific functions
from hello import greet, greet_multiple, Greeter

# Import entire module
import hello

# Use with module prefix
message = hello.greet("Alice")

# Import with alias
import hello as greeting_module
message = greeting_module.greet("Bob")
```

## Function Examples

### greet() Function

#### Basic Greeting

```python
from hello import greet

# Default greeting
result = greet("Alice")
print(result)
# Output: Hello, Alice!
```

#### Custom Greetings

```python
# Different greeting words
greetings = [
    greet("Alice", "Hi"),
    greet("Bob", "Welcome"),
    greet("Charlie", "Good morning"),
    greet("Diana", "Howdy")
]

for greeting in greetings:
    print(greeting)
# Output:
# Hi, Alice!
# Welcome, Bob!
# Good morning, Charlie!
# Howdy, Diana!
```

#### Handling Whitespace

```python
# Function automatically strips whitespace
result1 = greet("  Alice  ")
result2 = greet("\tBob\n")
result3 = greet("Charlie   ", "  Hi  ")

print(result1)  # Hello, Alice!
print(result2)  # Hello, Bob!
print(result3)  # Hi, Charlie!
```

### greet_multiple() Function

#### Basic Multiple Greetings

```python
from hello import greet_multiple

names = ["Alice", "Bob", "Charlie"]
greetings = greet_multiple(names)

for greeting in greetings:
    print(greeting)
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

#### Custom Greeting for Multiple People

```python
team_names = ["Sarah", "Mike", "Jennifer"]
welcome_messages = greet_multiple(team_names, "Welcome")

print("\n".join(welcome_messages))
# Output:
# Welcome, Sarah!
# Welcome, Mike!
# Welcome, Jennifer!
```

#### Empty List Handling

```python
# Handle empty lists gracefully
empty_greetings = greet_multiple([])
print(f"Number of greetings: {len(empty_greetings)}")
# Output: Number of greetings: 0
```

### greet_multiple_safe() Function

#### Handling Mixed Valid/Invalid Data

```python
from hello import greet_multiple_safe

# Mix of valid and invalid names
mixed_names = ["Alice", "", "Bob", None, "Charlie", "   ", "Diana"]
safe_greetings = greet_multiple_safe(mixed_names)

print(f"Generated {len(safe_greetings)} greetings:")
for greeting in safe_greetings:
    print(greeting)
# Output:
# Generated 3 greetings:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
# Hello, Diana!
```

#### Logging Example

```python
import logging
from hello import greet_multiple_safe

# Enable logging to see warnings
logging.basicConfig(level=logging.WARNING)

# This will log warnings for invalid names
names = ["Valid", "", None, "Also Valid"]
greetings = greet_multiple_safe(names)
# Logs warnings for empty string and None value
```

## Class Examples

### Greeter Class

#### Basic Usage

```python
from hello import Greeter

# Create a greeter with default settings
greeter = Greeter()

# Generate greetings
message1 = greeter.greet("Alice")
message2 = greeter.greet("Bob")

print(message1)  # Hello, Alice!
print(message2)  # Hello, Bob!

# Check history
print(f"Generated {len(greeter.greeting_history)} greetings")
# Output: Generated 2 greetings
```

#### Custom Default Greeting

```python
# Create greeter with custom default
morning_greeter = Greeter("Good morning")

messages = [
    morning_greeter.greet("Team"),
    morning_greeter.greet("Boss"),
    morning_greeter.greet("Client", "Welcome")  # Override default
]

for message in messages:
    print(message)
# Output:
# Good morning, Team!
# Good morning, Boss!
# Welcome, Client!
```

#### Case Sensitivity Options

```python
# Case sensitive (default)
case_sensitive_greeter = Greeter(case_sensitive=True)
message1 = case_sensitive_greeter.greet("john doe")
print(message1)  # Hello, john doe!

# Case insensitive
case_insensitive_greeter = Greeter(case_sensitive=False)
message2 = case_insensitive_greeter.greet("john doe")
print(message2)  # Hello, John Doe!
```

#### Statistics Tracking

```python
# Create greeter and generate various greetings
stats_greeter = Greeter()

# Generate greetings with different patterns
stats_greeter.greet("Alice")
stats_greeter.greet("Bob", "Hi")
stats_greeter.greet("Alice", "Welcome")  # Same name, different greeting
stats_greeter.greet("Charlie")

# Get statistics
stats = stats_greeter.get_statistics()
print(f"Total greetings: {stats['total_greetings']}")  # 4
print(f"Unique names: {stats['unique_names']}")        # 3
print(f"Most common greeting: {stats['most_common_greeting']}")  # Hello
```

#### History Management

```python
# Track and manage greeting history
history_greeter = Greeter("Hi")

# Generate some greetings
names = ["Alice", "Bob", "Charlie"]
for name in names:
    history_greeter.greet(name)

# View history
print("Greeting history:")
for i, greeting in enumerate(history_greeter.greeting_history, 1):
    print(f"{i}. {greeting}")
# Output:
# 1. Hi, Alice!
# 2. Hi, Bob!
# 3. Hi, Charlie!

# Clear history but keep settings
history_greeter.clear_history()
print(f"History after clear: {len(history_greeter.greeting_history)}")  # 0
print(f"Default greeting preserved: {history_greeter.default_greeting}")  # Hi
```

## Error Handling

### Handling Invalid Inputs

```python
from hello import greet, greet_multiple, Greeter

# Example 1: Empty name
try:
    result = greet("")
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Name cannot be empty or whitespace only

# Example 2: Wrong type
try:
    result = greet(123)
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: Name must be a string

# Example 3: Invalid list for multiple greetings
try:
    result = greet_multiple("not a list")
except TypeError as e:
    print(f"Error: {e}")
# Output: Error: Names must be a list

# Example 4: Invalid greeter initialization
try:
    greeter = Greeter("")
except ValueError as e:
    print(f"Error: {e}")
# Output: Error: Default greeting cannot be empty
```

### Robust Error Handling Pattern

```python
def safe_greeting_workflow(names, greeting="Hello"):
    """
    Example of robust error handling for greeting workflow.
    """
    results = {
        'successful_greetings': [],
        'failed_names': [],
        'errors': []
    }
    
    if not isinstance(names, list):
        names = [names]  # Convert single name to list
    
    for name in names:
        try:
            if isinstance(name, str) and name.strip():
                greeting_msg = greet(name, greeting)
                results['successful_greetings'].append(greeting_msg)
            else:
                results['failed_names'].append(name)
        except Exception as e:
            results['failed_names'].append(name)
            results['errors'].append(str(e))
    
    return results

# Test the robust workflow
test_names = ["Alice", "", 123, "Bob", None, "Charlie"]
results = safe_greeting_workflow(test_names)

print(f"Successful: {len(results['successful_greetings'])}")
print(f"Failed: {len(results['failed_names'])}")
for greeting in results['successful_greetings']:
    print(f"  {greeting}")
```

## Advanced Use Cases

### Multi-Language Greeting System

```python
from hello import Greeter

class MultiLanguageGreeter:
    """Extended greeter with multiple language support."""
    
    def __init__(self):
        self.greetings = {
            'english': 'Hello',
            'spanish': 'Hola',
            'french': 'Bonjour',
            'german': 'Guten Tag',
            'italian': 'Ciao'
        }
        self.greeters = {}
        
        # Create a greeter for each language
        for lang, greeting in self.greetings.items():
            self.greeters[lang] = Greeter(greeting)
    
    def greet(self, name, language='english'):
        """Greet in specified language."""
        if language not in self.greeters:
            raise ValueError(f"Unsupported language: {language}")
        return self.greeters[language].greet(name)
    
    def get_all_statistics(self):
        """Get statistics for all languages."""
        return {
            lang: greeter.get_statistics() 
            for lang, greeter in self.greeters.items()
        }

# Usage example
multi_greeter = MultiLanguageGreeter()

# Greet in different languages
greetings = [
    multi_greeter.greet("Alice", "english"),
    multi_greeter.greet("Carlos", "spanish"),
    multi_greeter.greet("Marie", "french"),
    multi_greeter.greet("Hans", "german"),
    multi_greeter.greet("Marco", "italian")
]

for greeting in greetings:
    print(greeting)
# Output:
# Hello, Alice!
# Hola, Carlos!
# Bonjour, Marie!
# Guten Tag, Hans!
# Ciao, Marco!
```

### Batch Processing Example

```python
from hello import greet_multiple_safe, Greeter
import csv
from io import StringIO

def process_greeting_batch(csv_data, default_greeting="Hello"):
    """
    Process a batch of names from CSV data.
    
    CSV format: name,custom_greeting (custom_greeting is optional)
    """
    # Parse CSV data
    reader = csv.DictReader(StringIO(csv_data))
    
    results = []
    greeter = Greeter(default_greeting)
    
    for row in reader:
        name = row.get('name', '').strip()
        custom_greeting = row.get('custom_greeting', '').strip()
        
        if name:
            try:
                if custom_greeting:
                    message = greeter.greet(name, custom_greeting)
                else:
                    message = greeter.greet(name)
                results.append({
                    'name': name,
                    'greeting': message,
                    'status': 'success'
                })
            except Exception as e:
                results.append({
                    'name': name,
                    'greeting': None,
                    'status': 'error',
                    'error': str(e)
                })
    
    return results, greeter.get_statistics()

# Example CSV data
csv_input = """name,custom_greeting
Alice,Hi
Bob,
Charlie,Welcome
,Invalid
David,Good morning"""

results, stats = process_greeting_batch(csv_input)

print("Processing Results:")
for result in results:
    if result['status'] == 'success':
        print(f"✓ {result['greeting']}")
    else:
        print(f"✗ Failed for '{result['name']}': {result.get('error', 'Unknown error')}")

print(f"\nStatistics: {stats}")
```

### Configuration-Driven Greeter

```python
from hello import Greeter
import json

class ConfigurableGreeter:
    """Greeter that can be configured via JSON."""
    
    def __init__(self, config_json):
        """Initialize from JSON configuration."""
        config = json.loads(config_json)
        
        self.default_greeting = config.get('default_greeting', 'Hello')
        self.case_sensitive = config.get('case_sensitive', True)
        self.custom_greetings = config.get('custom_greetings', {})
        
        self.greeter = Greeter(self.default_greeting, self.case_sensitive)
    
    def greet(self, name):
        """Greet with custom logic for specific names."""
        # Check for name-specific greetings
        custom_greeting = self.custom_greetings.get(name.lower())
        
        if custom_greeting:
            return self.greeter.greet(name, custom_greeting)
        else:
            return self.greeter.greet(name)

# Configuration example
config = """
{
    "default_greeting": "Welcome",
    "case_sensitive": false,
    "custom_greetings": {
        "boss": "Good morning",
        "client": "Greetings",
        "team": "Hi there"
    }
}
"""

configurable_greeter = ConfigurableGreeter(config)

# Test with different names
test_names = ["alice", "Boss", "CLIENT", "john", "Team"]
for name in test_names:
    greeting = configurable_greeter.greet(name)
    print(f"{name} -> {greeting}")
# Output:
# alice -> Welcome, Alice!
# Boss -> Good morning, Boss!
# CLIENT -> Greetings, Client!
# john -> Welcome, John!
# Team -> Hi there, Team!
```

## Integration Examples

### Web API Integration

```python
from hello import Greeter, greet_multiple_safe
from flask import Flask, request, jsonify

app = Flask(__name__)
api_greeter = Greeter("Welcome")

@app.route('/greet', methods=['POST'])
def api_greet():
    """API endpoint for single greeting."""
    data = request.get_json()
    name = data.get('name')
    custom_greeting = data.get('greeting')
    
    try:
        if custom_greeting:
            message = api_greeter.greet(name, custom_greeting)
        else:
            message = api_greeter.greet(name)
        
        return jsonify({
            'success': True,
            'message': message
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/greet/batch', methods=['POST'])
def api_greet_batch():
    """API endpoint for batch greetings."""
    data = request.get_json()
    names = data.get('names', [])
    greeting = data.get('greeting', 'Welcome')
    
    messages = greet_multiple_safe(names, greeting)
    
    return jsonify({
        'success': True,
        'greetings': messages,
        'count': len(messages)
    })

@app.route('/stats', methods=['GET'])
def api_stats():
    """API endpoint for greeting statistics."""
    stats = api_greeter.get_statistics()
    return jsonify(stats)

# Example usage (requires Flask to be installed):
# if __name__ == '__main__':
#     app.run(debug=True)
```

### Command Line Interface

```python
#!/usr/bin/env python3
"""
Command line interface for the hello module.
"""

import argparse
import sys
from hello import greet, greet_multiple_safe, Greeter

def main():
    parser = argparse.ArgumentParser(description='Greeting CLI tool')
    parser.add_argument('names', nargs='+', help='Names to greet')
    parser.add_argument('-g', '--greeting', default='Hello', 
                       help='Custom greeting (default: Hello)')
    parser.add_argument('--case-insensitive', action='store_true',
                       help='Convert names to title case')
    parser.add_argument('--stats', action='store_true',
                       help='Show statistics after greeting')
    
    args = parser.parse_args()
    
    # Create greeter
    greeter = Greeter(args.greeting, case_sensitive=not args.case_insensitive)
    
    # Process greetings
    for name in args.names:
        try:
            message = greeter.greet(name)
            print(message)
        except Exception as e:
            print(f"Error greeting '{name}': {e}", file=sys.stderr)
    
    # Show statistics if requested
    if args.stats:
        stats = greeter.get_statistics()
        print(f"\nStatistics:")
        print(f"  Total greetings: {stats['total_greetings']}")
        print(f"  Unique names: {stats['unique_names']}")
        print(f"  Most common greeting: {stats['most_common_greeting']}")

if __name__ == '__main__':
    main()

# Usage examples:
# python greeting_cli.py Alice Bob Charlie
# python greeting_cli.py --greeting "Hi" --stats Alice Bob
# python greeting_cli.py --case-insensitive alice bob charlie
```

## Performance Tips

### Efficient Batch Processing

```python
from hello import greet_multiple_safe
import time

def performance_comparison():
    """Compare different approaches for processing large batches."""
    names = [f"User{i}" for i in range(1000)]
    
    # Method 1: Using greet_multiple_safe (recommended)
    start_time = time.time()
    greetings1 = greet_multiple_safe(names)
    time1 = time.time() - start_time
    
    # Method 2: Individual greet calls
    start_time = time.time()
    greetings2 = []
    for name in names:
        try:
            greetings2.append(greet(name))
        except:
            pass
    time2 = time.time() - start_time
    
    print(f"greet_multiple_safe: {time1:.4f} seconds")
    print(f"Individual greet calls: {time2:.4f} seconds")
    print(f"Performance ratio: {time2/time1:.2f}x")

# performance_comparison()
```

### Memory-Efficient History Management

```python
from hello import Greeter

class MemoryEfficientGreeter(Greeter):
    """Greeter with configurable history limits."""
    
    def __init__(self, default_greeting="Hello", case_sensitive=True, max_history=100):
        super().__init__(default_greeting, case_sensitive)
        self.max_history = max_history
    
    def greet(self, name, greeting=None):
        """Greet with history size management."""
        message = super().greet(name, greeting)
        
        # Trim history if it exceeds limit
        if len(self.greeting_history) > self.max_history:
            self.greeting_history = self.greeting_history[-self.max_history:]
        
        return message

# Usage for long-running applications
efficient_greeter = MemoryEfficientGreeter(max_history=50)

# This will never use more than 50 items of memory for history
for i in range(200):
    efficient_greeter.greet(f"User{i}")

print(f"History size: {len(efficient_greeter.greeting_history)}")  # Will be 50
```

This completes the comprehensive examples and tutorials documentation. The examples progress from basic usage to advanced integration patterns, providing practical guidance for all levels of users.