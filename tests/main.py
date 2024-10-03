import sys
from calculator import Calculator

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    a, b, operation = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
        sys.exit(1)

    calc = Calculator()

    try:
        if operation == 'add':
            result = calc.add(a, b)
        elif operation == 'subtract':
            result = calc.subtract(a, b)
        elif operation == 'multiply':
            result = calc.multiply(a, b)
        elif operation == 'divide':
            result = calc.divide(a, b)
        else:
            print(f"Unknown operation: {operation}")
            sys.exit(1)

        print(f"The result of {a} {operation} {b} is equal to {result}")
    except ZeroDivisionError:
        print("An error occurred: Cannot divide by zero")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
