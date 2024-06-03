import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python eval.py <operation> <num1> <num2>")
    else:
        operation = sys.argv[1]
        num1 = int(sys.argv[2])
        num2 = int(sys.argv[3])

        if operation == 'add':
            result = eval(f"{num1} + {num2}")
            print(f"The sum of {num1} and {num2} is: {result}")
        elif operation == 'subtract':
            result = eval(f"{num1} - {num2}")
            print(f"The difference of {num1} and {num2} is: {result}")
        elif operation == 'product':
            result = eval(f"{num1} * {num2}")
            print(f"The product of {num1} and {num2} is: {result}")
        elif operation == 'divide':
            if num2 == 0:
                print("Error: Cannot divide by zero")
            else:
                result = eval(f"{num1} / {num2}")
                print(f"The division of {num1} by {num2} is: {result}")
        else:
            print("Invalid operation. Please choose from 'add', 'subtract', 'product', or 'divide'")