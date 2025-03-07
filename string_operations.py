def reverse_string(s):
    return s[::-1]

def to_uppercase(s):
    return s.upper()

def to_lowercase(s):
    return s.lower()

if __name__ == "__main__":
    text = "Hello World"
    print("Original:", text)  # Already using print function syntax, no change needed
    print("Reversed:", reverse_string(text))  # Already using print function syntax, no change needed
    print("Uppercase:", to_uppercase(text))  # Already using print function syntax, no change needed
    print("Lowercase:", to_lowercase(text))  # Already using print function syntax, no change needed