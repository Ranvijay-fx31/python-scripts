import random
import string
import json
import requests
from bs4 import BeautifulSoup  # Already using Python 3 import style

# ---------------------- Basic Calculations ----------------------
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Cannot divide by zero"  # In Python 3, / always returns float
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
    return (celsius * 9/5) + 32  # In Python 3, / always returns float

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # In Python 3, / always returns float

# ---------------------- Basic Web Scraper ----------------------
def get_website_title(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string
    return "Failed to retrieve"

# ---------------------- File Handling ----------------------
def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:  # Exception syntax is already Python 3 compatible
        return "File not found"

# ---------------------- JSON File Handling ----------------------
def write_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def read_json(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:  # Exception syntax is already Python 3 compatible
        return "File not found"

# ---------------------- Random Number Generator ----------------------
def generate_random_numbers(count=5, start=1, end=100):
    return [random.randint(start, end) for _ in range(count)]  # range in Python 3 behaves like xrange in Python 2

# ---------------------- Reverse Text ----------------------
def reverse_text(text):
    return text[::-1]

# ---------------------- Sorting Algorithms ----------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # range in Python 3 behaves like xrange in Python 2
        for j in range(0, n-i-1):  # range in Python 3 behaves like xrange in Python 2
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # // for integer division is the same in Python 2 and 3
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ---------------------- Simple Quiz Game ----------------------
def simple_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 5 + 5?": "10",
        "Who wrote 'Hamlet'?": "Shakespeare"
    }
    score = 0
    for question, answer in questions.items():  # .items() in Python 3 behaves like .iteritems() in Python 2
        user_answer = input(question + " ")  # Changed from raw_input() to input() for Python 3
        if user_answer.lower() == answer.lower():
            score += 1
    return f"You got {score}/{len(questions)} correct!"

# ---------------------- Basic Encryption (Caesar Cipher) ----------------------
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# ---------------------- Run Tests ----------------------
if __name__ == "__main__":
    print("\nCalculator:", calculator(10, 5, "add"))  # Changed to print() function call
    print("Is 17 Prime?", is_prime(17))  # Changed to print() function call
    print("Is 'madam' a Palindrome?", is_palindrome("madam"))  # Changed to print() function call
    print("Fibonacci Sequence:", fibonacci(10))  # Changed to print() function call
    print("Factorial of 5:", factorial(5))  # Changed to print() function call

    add_task("Learn Python")
    add_task("Push code to GitHub")
    print("\nTo-Do List:\n", list_tasks())  # Changed to print() function call

    print("\nGenerated Password:", generate_password(12))  # Changed to print() function call
    print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))  # Changed to print() function call
    print("77°F to Celsius:", fahrenheit_to_celsius(77))  # Changed to print() function call

    print("\nWebsite Title:", get_website_title("https://www.example.com"))  # Changed to print() function call

    print("\nReverse Text:", reverse_text("Hello World"))  # Changed to print() function call
    print("Bubble Sort:", bubble_sort([5, 3, 8, 1, 2]))  # Changed to print() function call
    print("Quick Sort:", quick_sort([5, 3, 8, 1, 2]))  # Changed to print() function call

    print("\nEncrypted Text:", caesar_cipher("Hello", 3))  # Changed to print() function call

    # Uncomment below to play quiz:
    # print(simple_quiz())  # Changed to print() function call