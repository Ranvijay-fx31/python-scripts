def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b  # In Python 3, this is true division (returns float)
                  # In Python 2, this would perform integer division for integer inputs
                  # No change needed as true division is likely the intended behavior

if __name__ == "__main__":
    # Updated print statements to use function syntax as required in Python 3
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Multiplication:", multiply(5, 3))
    print("Division:", divide(5, 3))