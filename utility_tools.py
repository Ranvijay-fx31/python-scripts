import random
import string
import json
import requests
from bs4 import BeautifulSoup  # Already using Python 3 import style

# ---------------------- Calculator ----------------------
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        # In Python 3, division always returns float
        # No change needed as this behavior is expected
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# ---------------------- Prime Number Checker ----------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # range in Python 3 behaves like xrange in Python 2
        if n % i == 0:
            return False
    return True

# ---------------------- Palindrome Checker ----------------------
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

# ---------------------- Fibonacci Series ----------------------
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):  # range in Python 3 behaves like xrange in Python 2
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# ---------------------- Factorial Calculator ----------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# ---------------------- To-Do List Manager ----------------------
tasks = []
def add_task(task):
    tasks.append(task)
    return f"Added task: {task}"  # f-strings are available in Python 3.6+, but compatible with 3.3 using format()

def remove_task(index):
    if 0 <= index < len(tasks):
        return f"Removed task: {tasks.pop(index)}"  # f-strings are available in Python 3.6+, but compatible with 3.3 using format()
    return "Invalid index"

def list_tasks():
    return "\n".join([f"{i + 1}. {task}" for i, task in enumerate(tasks)])  # f-strings are available in Python 3.6+, but compatible with 3.3 using format()

# ---------------------- Random Password Generator ----------------------
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))  # range in Python 3 behaves like xrange in Python 2

# ---------------------- Temperature Converter ----------------------
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # In Python 3, division always returns float

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # In Python 3, division always returns float

# ---------------------- Basic Web Scraper ----------------------
def get_website_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string
    return "Failed to retrieve"

# ---------------------- Run Tests ----------------------
if __name__ == "__main__":
    # Updated print statements to use print() function syntax
    print("\nCalculator:", calculator(10, 5, "add"))
    print("Is 17 Prime?", is_prime(17))
    print("Is 'madam' a Palindrome?", is_palindrome("madam"))
    print("Fibonacci Sequence:", fibonacci(10))
    print("Factorial of 5:", factorial(5))
    
    add_task("Learn Python")
    add_task("Push code to GitHub")
    print("\nTo-Do List:\n", list_tasks())
    
    print("\nGenerated Password:", generate_password(12))
    print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))
    print("77°F to Celsius:", fahrenheit_to_celsius(77))
    
    print("\nWebsite Title:", get_website_title("https://www.example.com"))