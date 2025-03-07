def write_to_file(filename, text):
    # Added encoding parameter for better handling of non-ASCII characters in Python 3
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def read_from_file(filename):
    try:
        # Added encoding parameter for better handling of non-ASCII characters in Python 3
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        # FileNotFoundError is already compatible with Python 3, no change needed
        return "File not found"

if __name__ == "__main__":
    filename = "sample.txt"
    write_to_file(filename, "Hello, this is a test file.")
    # Updated print statement to use function syntax as required in Python 3
    print("File Content:", read_from_file(filename))