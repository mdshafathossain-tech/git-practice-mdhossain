# Functions to perform basic math operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Please provide numerical inputs."
    
def square(a):
    return a * a