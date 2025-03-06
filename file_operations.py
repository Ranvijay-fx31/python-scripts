def write_to_file(filename, text):
    with open(filename, "w") as file:
        file.write(text)

def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    filename = "sample.txt"
    write_to_file(filename, "Hello, this is a test file.")
    print("File Content:", read_from_file(filename))
