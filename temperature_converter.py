def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Division in Python 3 always returns float, no change needed

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # Division in Python 3 always returns float, no change needed

if __name__ == "__main__":
    # Updated print statements to use print() function syntax for Python 3
    print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))
    print("77°F to Celsius:", fahrenheit_to_celsius(77))