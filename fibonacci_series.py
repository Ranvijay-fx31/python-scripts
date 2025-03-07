def fibonacci(n):
    sequence = [0, 1]
    for _ in range(n - 2):  # range in Python 3 behaves like xrange in Python 2
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

if __name__ == "__main__":
    print("Fibonacci Series:", fibonacci(10))  # print is now a function in Python 3