import random

def generate_random_numbers(count=5, start=1, end=100):
    return [random.randint(start, end) for _ in range(count)]

if __name__ == "__main__":
    print("Random Numbers:", generate_random_numbers())
