def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    text = "madam"
    print(f"Is '{text}' a palindrome?", is_palindrome(text))
