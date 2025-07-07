# Contributing Guide

Thank you for your interest in contributing to the repo-demo project! This guide provides comprehensive information about contributing code, documentation, and following our development standards.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Standards](#code-standards)
- [Documentation Standards](#documentation-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- Basic understanding of Python development practices

### Development Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/your-username/repo-demo.git
   cd repo-demo
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Development Dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Verify Setup**
   ```bash
   python hello.py
   python -m pytest tests/
   ```

## Code Standards

### Python Style Guide

We follow **PEP 8** with some specific guidelines:

#### Code Formatting

- **Line Length**: Maximum 88 characters (Black default)
- **Indentation**: 4 spaces (no tabs)
- **Quotes**: Double quotes for strings, single for characters
- **Imports**: Grouped and sorted (isort)

#### Tools

Use these tools to maintain code quality:

```bash
# Format code
black .

# Sort imports
isort .

# Lint code
flake8 .

# Type checking
mypy .
```

#### Example Code Style

```python
from typing import List, Optional, Union
import logging

logger = logging.getLogger(__name__)


def example_function(
    param1: str, 
    param2: Optional[int] = None,
    *args,
    **kwargs
) -> str:
    """
    Example function following our style guidelines.
    
    Args:
        param1: First parameter description
        param2: Optional second parameter
        *args: Variable length argument list
        **kwargs: Arbitrary keyword arguments
    
    Returns:
        Formatted string result
    
    Raises:
        ValueError: When param1 is empty
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    
    logger.info(f"Processing {param1}")
    
    result = f"Processed: {param1}"
    if param2 is not None:
        result += f" (value: {param2})"
    
    return result
```

### Naming Conventions

- **Functions/Variables**: `snake_case`
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`
- **Private attributes**: Leading underscore `_private`
- **Protected attributes**: Single underscore `_protected`

## Documentation Standards

### Docstring Format

We use **Google-style docstrings** for all public functions and classes:

```python
def function_name(param1: str, param2: int = 0) -> str:
    """
    Brief description of the function.
    
    Longer description if needed. Explain the purpose, behavior,
    and any important implementation details.
    
    Args:
        param1 (str): Description of the first parameter.
        param2 (int, optional): Description of the second parameter.
            Defaults to 0.
    
    Returns:
        str: Description of the return value and its format.
    
    Raises:
        ValueError: When and why this exception is raised.
        TypeError: When and why this exception is raised.
    
    Example:
        Basic usage example:
        
        >>> result = function_name("hello", 42)
        >>> print(result)
        "hello_42"
        
        Advanced usage:
        
        >>> result = function_name("world")
        >>> print(result)
        "world_0"
    
    Note:
        Any additional notes, warnings, or implementation details.
    """
```

### Class Documentation

```python
class ExampleClass:
    """
    Brief description of the class.
    
    Longer description explaining the purpose, main functionality,
    and usage patterns of the class.
    
    Attributes:
        public_attr (str): Description of public attribute.
        another_attr (int): Description of another attribute.
    
    Example:
        Basic usage of the class:
        
        >>> obj = ExampleClass("value")
        >>> result = obj.method()
        >>> print(result)
        "processed_value"
    """
    
    def __init__(self, initial_value: str):
        """
        Initialize a new ExampleClass instance.
        
        Args:
            initial_value (str): The initial value to store.
        
        Raises:
            ValueError: If initial_value is empty.
        """
```

### Type Hints

- **Always use type hints** for all public functions and methods
- Use `typing` module for complex types
- Be specific: use `List[str]` instead of just `list`
- Use `Optional[T]` for parameters that can be None

```python
from typing import List, Optional, Dict, Union, Callable

def complex_function(
    items: List[str],
    mapping: Dict[str, int],
    callback: Optional[Callable[[str], bool]] = None,
    flags: Union[str, List[str]] = None
) -> Dict[str, Union[int, str]]:
    """Function with comprehensive type hints."""
```

### Documentation Requirements

For all new code contributions:

1. **Module docstring** at the top of each file
2. **Function docstrings** for all public functions
3. **Class docstrings** for all classes
4. **Method docstrings** for all public methods
5. **Type hints** for all parameters and return values
6. **Examples** in docstrings for complex functionality
7. **Update API_REFERENCE.md** for new public APIs

## Testing Guidelines

### Test Structure

Create tests in the `tests/` directory:

```
tests/
├── __init__.py
├── test_hello.py
├── test_greeter.py
└── conftest.py
```

### Test Writing Standards

```python
import pytest
from hello import greet, Greeter


class TestGreetFunction:
    """Test cases for the greet function."""
    
    def test_basic_greeting(self):
        """Test basic greeting functionality."""
        result = greet("World")
        assert result == "Hello, World!"
    
    def test_custom_greeting(self):
        """Test greeting with custom message."""
        result = greet("Alice", "Hi")
        assert result == "Hi, Alice!"
    
    def test_empty_name_raises_error(self):
        """Test that empty names raise ValueError."""
        with pytest.raises(ValueError, match="cannot be empty"):
            greet("")
    
    def test_name_type_validation(self):
        """Test that non-string names raise TypeError."""
        with pytest.raises(TypeError, match="must be a string"):
            greet(123)


class TestGreeterClass:
    """Test cases for the Greeter class."""
    
    @pytest.fixture
    def greeter(self):
        """Create a Greeter instance for testing."""
        return Greeter("Hello")
    
    def test_initialization(self, greeter):
        """Test Greeter initialization."""
        assert greeter.default_greeting == "Hello"
        assert greeter.case_sensitive is True
        assert len(greeter.greeting_history) == 0
```

### Test Coverage

- Aim for **90%+ code coverage**
- Test all public functions and methods
- Test error conditions and edge cases
- Test parameter validation
- Include integration tests for complex workflows

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=hello --cov-report=html

# Run specific test file
pytest tests/test_hello.py

# Run specific test
pytest tests/test_hello.py::TestGreetFunction::test_basic_greeting
```

## Pull Request Process

### Before Submitting

1. **Run all checks**:
   ```bash
   black .
   isort .
   flake8 .
   mypy .
   pytest --cov=hello
   ```

2. **Update documentation**:
   - Add/update docstrings
   - Update API_REFERENCE.md
   - Update README.md if needed

3. **Add tests** for new functionality

### PR Guidelines

1. **Branch naming**: `feature/description` or `fix/description`
2. **Commit messages**: Use conventional commits format
3. **PR title**: Clear and descriptive
4. **PR description**: Include:
   - What changes were made
   - Why the changes were necessary
   - How to test the changes
   - Any breaking changes

### Example PR Description

```markdown
## Summary

Add support for case-insensitive name handling in the Greeter class.

## Changes

- Added `case_sensitive` parameter to Greeter constructor
- Modified `greet()` method to handle case conversion
- Added comprehensive tests for new functionality
- Updated documentation and examples

## Testing

```bash
pytest tests/test_greeter.py::TestGreeterClass::test_case_insensitive
```

## Breaking Changes

None - this is a backward-compatible addition.
```

## Issue Reporting

### Bug Reports

Use the bug report template and include:

- **Python version**
- **Operating system**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Error messages/stack traces**

### Feature Requests

Use the feature request template and include:

- **Use case description**
- **Proposed solution**
- **Alternative solutions considered**
- **Example usage**

### Documentation Issues

- Clearly describe what documentation is missing or incorrect
- Suggest improvements or additions
- Provide examples if applicable

## Development Workflow

### Standard Workflow

1. **Create Issue** (for bugs or features)
2. **Create Branch** from main
3. **Implement Changes** following standards
4. **Add Tests** and documentation
5. **Run Quality Checks**
6. **Submit Pull Request**
7. **Address Review Comments**
8. **Merge** after approval

### Quality Gates

All PRs must pass:

- ✅ Code formatting (Black, isort)
- ✅ Linting (flake8)
- ✅ Type checking (mypy)
- ✅ Tests (pytest with 90%+ coverage)
- ✅ Documentation completeness
- ✅ Code review approval

## Questions and Support

- **Questions**: Open a discussion on GitHub
- **Documentation**: Check API_REFERENCE.md first
- **Bugs**: Use the issue tracker
- **Features**: Submit feature request issue

Thank you for contributing to repo-demo! 🚀