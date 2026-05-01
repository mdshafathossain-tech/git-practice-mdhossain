# Functions to perform basic math operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    # Error handling: prevents the program from crashing if b is 0
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b