def write_to_file(filename, text):
    # In Python 3, it's recommended to specify encoding for text files
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def read_from_file(filename):
    try:
        # In Python 3, it's recommended to specify encoding for text files
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    filename = "sample.txt"
    write_to_file(filename, "Hello, this is a test file.")
    # Changed print statement to print() function call as required in Python 3
    print("File Content:", read_from_file(filename))