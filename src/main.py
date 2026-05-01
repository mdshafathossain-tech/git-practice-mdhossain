import datetime
# Import all four functions from your utils file
from utils import add, subtract, multiply, divide

def run_calculator_tests():
    name = "MD Hossain"
    today = datetime.date.today()

    print(f"--- Calculator Project ---")
    print(f"Developer: {name}")
    print(f"Date: {today}")
    print("---------------------------")

    # Defining test numbers
    num1 = 10
    num2 = 5

    # Executing and printing all operations
    print(f"Addition:       {num1} + {num2} = {add(num1, num2)}")
    print(f"Subtraction:    {num1} - {num2} = {subtract(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
    print(f"Division:       {num1} / {num2} = {divide(num1, num2)}")
    
    # Testing Division by Zero
    print(f"Division (0):   {num1} / 0 = {divide(num1, 0)}")

if __name__ == "__main__":
    run_calculator_tests()