"""
Hello World Module

A demonstration module for the Agentic AI course showcasing proper Python
documentation standards and API design patterns.

This module provides basic greeting functionality and serves as an example
of well-documented Python code.

Example:
    Basic usage of the hello module:
    
    >>> from hello import greet, greet_multiple
    >>> message = greet("World")
    >>> print(message)
    Hello, World!
    
    >>> messages = greet_multiple(["Alice", "Bob"])
    >>> print(messages)
    ['Hello, Alice!', 'Hello, Bob!']

Author: Agentic AI Course
Version: 1.0.0
"""

from typing import List, Optional, Union
import logging

# Configure logging for the module
logger = logging.getLogger(__name__)


def greet(name: str, greeting: str = "Hello") -> str:
    """
    Generate a personalized greeting message.
    
    This function creates a formatted greeting message by combining a greeting
    word with a person's name. It's the core function of the hello module.
    
    Args:
        name (str): The name of the person to greet. Must not be empty.
        greeting (str, optional): The greeting word to use. Defaults to "Hello".
    
    Returns:
        str: A formatted greeting message in the format "{greeting}, {name}!"
    
    Raises:
        ValueError: If name is empty or contains only whitespace.
        TypeError: If name or greeting is not a string.
    
    Example:
        >>> greet("World")
        'Hello, World!'
        
        >>> greet("Alice", "Hi")
        'Hi, Alice!'
        
        >>> greet("Bob", "Good morning")
        'Good morning, Bob!'
    
    Note:
        The function automatically adds punctuation (!) to the end of the message.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    
    if not isinstance(greeting, str):
        raise TypeError("Greeting must be a string")
    
    if not name or not name.strip():
        raise ValueError("Name cannot be empty or whitespace only")
    
    logger.info(f"Generating greeting for {name}")
    return f"{greeting}, {name.strip()}!"


def greet_multiple(names: List[str], greeting: str = "Hello") -> List[str]:
    """
    Generate greeting messages for multiple people.
    
    This function takes a list of names and generates individual greeting
    messages for each person using the specified greeting.
    
    Args:
        names (List[str]): A list of names to greet. Can be empty.
        greeting (str, optional): The greeting word to use. Defaults to "Hello".
    
    Returns:
        List[str]: A list of formatted greeting messages, one for each valid name.
    
    Raises:
        TypeError: If names is not a list or greeting is not a string.
        ValueError: If any name in the list is invalid (empty or not a string).
    
    Example:
        >>> greet_multiple(["Alice", "Bob", "Charlie"])
        ['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']
        
        >>> greet_multiple(["John"], "Hi")
        ['Hi, John!']
        
        >>> greet_multiple([])
        []
    
    Note:
        Invalid names in the list will cause the entire function to fail.
        Use greet_multiple_safe() if you want to skip invalid names.
    """
    if not isinstance(names, list):
        raise TypeError("Names must be a list")
    
    if not isinstance(greeting, str):
        raise TypeError("Greeting must be a string")
    
    logger.info(f"Generating greetings for {len(names)} people")
    
    greetings = []
    for name in names:
        greetings.append(greet(name, greeting))
    
    return greetings


def greet_multiple_safe(names: List[str], greeting: str = "Hello") -> List[str]:
    """
    Generate greeting messages for multiple people, skipping invalid names.
    
    This function is similar to greet_multiple() but silently skips any
    invalid names instead of raising an exception.
    
    Args:
        names (List[str]): A list of names to greet. Invalid names are skipped.
        greeting (str, optional): The greeting word to use. Defaults to "Hello".
    
    Returns:
        List[str]: A list of formatted greeting messages for valid names only.
    
    Raises:
        TypeError: If names is not a list or greeting is not a string.
    
    Example:
        >>> greet_multiple_safe(["Alice", "", "Bob", None, "Charlie"])
        ['Hello, Alice!', 'Hello, Bob!', 'Hello, Charlie!']
        
        >>> greet_multiple_safe(["", " ", None])
        []
    
    Note:
        This function logs warnings for skipped invalid names.
    """
    if not isinstance(names, list):
        raise TypeError("Names must be a list")
    
    if not isinstance(greeting, str):
        raise TypeError("Greeting must be a string")
    
    greetings = []
    skipped_count = 0
    
    for name in names:
        try:
            if isinstance(name, str) and name.strip():
                greetings.append(greet(name, greeting))
            else:
                skipped_count += 1
                logger.warning(f"Skipping invalid name: {repr(name)}")
        except (ValueError, TypeError):
            skipped_count += 1
            logger.warning(f"Skipping invalid name: {repr(name)}")
    
    logger.info(f"Generated {len(greetings)} greetings, skipped {skipped_count} invalid names")
    return greetings


class Greeter:
    """
    A class for managing personalized greetings with customizable settings.
    
    The Greeter class provides a stateful way to generate greetings with
    configurable default settings and the ability to track greeting history.
    
    Attributes:
        default_greeting (str): The default greeting to use when none is specified.
        greeting_history (List[str]): A history of all greetings generated.
        case_sensitive (bool): Whether to preserve the case of names.
    
    Example:
        >>> greeter = Greeter("Hi")
        >>> message = greeter.greet("World")
        >>> print(message)
        Hi, World!
        
        >>> greeter.greeting_history
        ['Hi, World!']
        
        >>> greeter.get_statistics()
        {'total_greetings': 1, 'unique_names': 1, 'most_common_greeting': 'Hi'}
    """
    
    def __init__(self, default_greeting: str = "Hello", case_sensitive: bool = True):
        """
        Initialize a new Greeter instance.
        
        Args:
            default_greeting (str, optional): Default greeting to use. Defaults to "Hello".
            case_sensitive (bool, optional): Whether to preserve name case. Defaults to True.
        
        Raises:
            TypeError: If default_greeting is not a string.
            ValueError: If default_greeting is empty.
        """
        if not isinstance(default_greeting, str):
            raise TypeError("Default greeting must be a string")
        
        if not default_greeting.strip():
            raise ValueError("Default greeting cannot be empty")
        
        self.default_greeting = default_greeting.strip()
        self.case_sensitive = case_sensitive
        self.greeting_history: List[str] = []
        
        logger.info(f"Initialized Greeter with default greeting: {self.default_greeting}")
    
    def greet(self, name: str, greeting: Optional[str] = None) -> str:
        """
        Generate a greeting message using the class settings.
        
        Args:
            name (str): The name of the person to greet.
            greeting (str, optional): Custom greeting. Uses default if None.
        
        Returns:
            str: The formatted greeting message.
        
        Raises:
            ValueError: If name is empty or invalid.
            TypeError: If name or greeting is not a string.
        """
        if greeting is None:
            greeting = self.default_greeting
        
        if not self.case_sensitive and isinstance(name, str):
            name = name.title()
        
        message = greet(name, greeting)
        self.greeting_history.append(message)
        
        return message
    
    def get_statistics(self) -> dict:
        """
        Get statistics about the greetings generated.
        
        Returns:
            dict: A dictionary containing statistics about greeting usage.
                Keys include: 'total_greetings', 'unique_names', 'most_common_greeting'
        
        Example:
            >>> greeter = Greeter()
            >>> greeter.greet("Alice")
            >>> greeter.greet("Bob")
            >>> stats = greeter.get_statistics()
            >>> print(stats['total_greetings'])
            2
        """
        from collections import Counter
        
        total = len(self.greeting_history)
        
        if total == 0:
            return {
                'total_greetings': 0,
                'unique_names': 0,
                'most_common_greeting': None
            }
        
        # Extract greeting words from history
        greeting_words = [msg.split(',')[0] for msg in self.greeting_history]
        greeting_counter = Counter(greeting_words)
        most_common = greeting_counter.most_common(1)[0][0]
        
        # Extract names (between comma and exclamation)
        names = [msg.split(', ')[1].rstrip('!') for msg in self.greeting_history]
        unique_names = len(set(names))
        
        return {
            'total_greetings': total,
            'unique_names': unique_names,
            'most_common_greeting': most_common
        }
    
    def clear_history(self) -> None:
        """
        Clear the greeting history.
        
        This method removes all stored greeting history but preserves
        the greeter's configuration settings.
        """
        logger.info(f"Clearing greeting history ({len(self.greeting_history)} items)")
        self.greeting_history.clear()


def main() -> None:
    """
    Main function demonstrating the hello module functionality.
    
    This function serves as an example of how to use the various functions
    and classes provided by the hello module.
    """
    print("Hello Module Demo")
    print("=" * 20)
    
    # Basic greeting examples
    print("\n1. Basic Greetings:")
    print(greet("World"))
    print(greet("Python", "Welcome"))
    
    # Multiple greetings
    print("\n2. Multiple Greetings:")
    names = ["Alice", "Bob", "Charlie"]
    greetings = greet_multiple(names)
    for greeting in greetings:
        print(greeting)
    
    # Greeter class example
    print("\n3. Greeter Class:")
    greeter = Greeter("Good morning")
    print(greeter.greet("Developer"))
    print(greeter.greet("User", "Welcome"))
    
    # Statistics
    print("\n4. Statistics:")
    stats = greeter.get_statistics()
    print(f"Total greetings: {stats['total_greetings']}")
    print(f"Unique names: {stats['unique_names']}")


if __name__ == "__main__":
    main()
