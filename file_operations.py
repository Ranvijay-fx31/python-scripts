"""
File operations module for reading and writing text files.
"""

def write_to_file(filename, text):
    """
    Write text content to a file.
    
    Args:
        filename (str): The path to the file to write to
        text (str): The content to write to the file
    """
    with open(filename, "w") as file:
        file.write(text)

def read_from_file(filename):
    """
    Read text content from a file.
    
    Args:
        filename (str): The path to the file to read from
        
    Returns:
        str: The file content or error message if file not found
    """
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

if __name__ == "__main__":
    # Example usage of the file operations
    filename = "sample.txt"
    write_to_file(filename, "Hello, this is a test file.")
    print(f"File Content: {read_from_file(filename)}")