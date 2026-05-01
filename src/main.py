import datetime
from utils import add, subtract  # This imports your functions from utils.py

name = "MD Shafat Hossain"
today = datetime.date.today()

print(f"Hello, my name is {name}")
print(f"Today's date is {today}")

# Testing the new calculator functions
print(f"Addition Result: 5 + 10 = {add(5, 10)}")
print(f"Subtraction Result: 20 - 7 = {subtract(20, 7)}")

print(f"Subtraction Test: 20 - 5 = {subtract(20, 5)}")

print(f"Multiplication Test: 4 * 3 = {multiply(4, 3)}")