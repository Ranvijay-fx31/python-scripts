def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b  # In Python 3, division always returns float, so no change needed here

if __name__ == "__main__":
    print("Addition:", add(5, 3))  # Updated to use print function syntax
    print("Subtraction:", subtract(5, 3))  # Updated to use print function syntax
    print("Multiplication:", multiply(5, 3))  # Updated to use print function syntax
    print("Division:", divide(5, 3))  # Updated to use print function syntax