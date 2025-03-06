def write_to_file(filename, text):
    # In Python 3, text files are opened in text mode by default, which handles Unicode
    # No change needed here as the code already uses the context manager pattern
    with open(filename, "w") as file:
        file.write(text)

def read_from_file(filename):
    try:
        # In Python 3, text files are opened in text mode by default, which handles Unicode
        # No change needed here as the code already uses the context manager pattern
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        # FileNotFoundError is correct in Python 3 (was IOError in Python 2)
        return "File not found"

if __name__ == "__main__":
    filename = "sample.txt"
    write_to_file(filename, "Hello, this is a test file.")
    # Print statement already uses parentheses, which is required in Python 3
    print("File Content:", read_from_file(filename))