import sys

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python cal.py <operation> <num1> <num2>")
    else:
        operation = sys.argv[1]
        num1 = int(sys.argv[2])
        num2 = int(sys.argv[3])

        if operation == 'add':
            result = add(num1, num2)
            print(f"The sum of {num1} and {num2} is: {result}")
        elif operation == 'subtract':
            result = subtract(num1, num2)
            print(f"The difference of {num1} and {num2} is: {result}")
        elif operation == 'product':
            result = product(num1, num2)
            print(f"The product of {num1} and {num2} is: {result}")
        elif operation == 'divide':
            result = divide(num1, num2)
            print(f"The division of {num1} by {num2} is: {result}")
        else:
            print("Invalid operation. Please choose from 'add', 'subtract', 'product', or 'divide'.")