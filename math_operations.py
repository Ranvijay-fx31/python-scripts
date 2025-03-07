"""
Mathematical operations module providing basic arithmetic functions.
"""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """
    Return the quotient of two numbers.
    
    Args:
        a: The dividend
        b: The divisor
        
    Returns:
        The quotient or an error message if divisor is zero
    """
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    # Example usage of arithmetic functions
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))