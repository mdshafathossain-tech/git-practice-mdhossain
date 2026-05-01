import datetime
from utils import add, subtract, multiply, divide

name = "MD Shafat Hossain"
today = datetime.date.today()

print(f"Hello, my name is {name}")
print(f"Today's date is {today}")

# Testing all functions
print(f"Add: 10 + 5 = {add(10, 5)}")
print(f"Subtract: 10 - 5 = {subtract(10, 5)}")
print(f"Multiply: 10 * 5 = {multiply(10, 5)}")
print(f"Divide: 10 / 2 = {divide(10, 2)}")