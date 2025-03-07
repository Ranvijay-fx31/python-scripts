def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    text = "madam"
    # Changed print statement to use print function with parentheses
    # Removed f-string as it's not supported in Python 3.3 (only in 3.6+)
    print("Is '{}' a palindrome?".format(text), is_palindrome(text))