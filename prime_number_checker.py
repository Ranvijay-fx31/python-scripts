def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    number = 17
    # Changed print statement to use print function with proper formatting
    # Removed f-string as it's not supported in Python 3.3 (only in 3.6+)
    print("Is {} a prime number? {}".format(number, is_prime(number)))