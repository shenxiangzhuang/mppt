"""Hello World module."""


def hello() -> str:
    """Returns a greeting.

    Returns:
        str: Hello, World!

    Examples:
        >>> hello()
        'Hello, World!'
    """
    return "Hello, World!"


def add(a: float, b: float) -> float:
    """Adds two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b

    Examples:
        >>> add(1, 2)
        3
        >>> add(2, 3)
        5
    """
    return a + b
