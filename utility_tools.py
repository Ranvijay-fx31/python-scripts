import random
import string
import json
import requests
from bs4 import BeautifulSoup

# ---------------------- Calculator ----------------------
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"
    else:
        return "Invalid operation"

# ---------------------- Prime Number Checker ----------------------
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
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
    for _ in range(n - 2):
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
    return f"Added task: {task}"

def remove_task(index):
    if 0 <= index < len(tasks):
        return f"Removed task: {tasks.pop(index)}"
    return "Invalid index"

def list_tasks():
    return "\n".join([f"{i + 1}. {task}" for i, task in enumerate(tasks)])

# ---------------------- Random Password Generator ----------------------
def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

# ---------------------- Temperature Converter ----------------------
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# ---------------------- Basic Web Scraper ----------------------
def get_website_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string
    return "Failed to retrieve"

# ---------------------- Run Tests ----------------------
if __name__ == "__main__":
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
