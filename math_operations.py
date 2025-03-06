def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    # In Python 3, division (/) always returns a float, unlike Python 2 where it performed integer division
    # No change needed here as the behavior is expected in Python 3
    return a / b

if __name__ == "__main__":
    # Print statements in Python 3 require parentheses, but they were already present in the original code
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))