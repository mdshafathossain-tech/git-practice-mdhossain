import datetime
from utils import add, subtract, multiply, divide

def run_tests():
    name = "MD Shafat Hossain"
    print(f"Developer: {name}")
    print(f"Date: {datetime.date.today()}")
    
    # Example calculations
    print(f"Addition: {add(10, 5)}")
    print(f"Division by Zero Test: {divide(10, 0)}")

if __name__ == "__main__":
    run_tests()