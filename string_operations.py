def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

if __name__ == "__main__":
    text = "Hello World"
    print("Original:", text)
    print("Reversed:", reverse_string(text))
    print("Uppercase:", to_uppercase(text))
    print("Lowercase:", to_lowercase(text))
