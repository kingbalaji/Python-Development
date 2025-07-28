class AdvancedCalculator:
    def power(self, x, y):
        return x ** y

    def sqrt(self, x):
        import math
        if x < 0:
            return "Cannot take square root of negative number"
        return math.sqrt(x)


class IntermediateCalculator(AdvancedCalculator):
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y


class Calculator(IntermediateCalculator):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


def main():
    calc = Calculator()

    operations = {
        '1': ('Addition', calc.add, 2),
        '2': ('Subtraction', calc.subtract, 2),
        '3': ('Multiplication', calc.multiply, 2),
        '4': ('Division', calc.divide, 2),
        '5': ('Power', calc.power, 2),
        '6': ('Square Root', calc.sqrt, 1)
    }

    while True:
        print("\nChoose operation:")
        for key, (name, _, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter choice: ")
        if choice not in operations:
            print("Invalid choice! Please try again.")
            continue

        op_name, func, num_args = operations[choice]

        try:
            if num_args == 2:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                result = func(x, y)
            else:
                x = float(input("Enter number: "))
                result = func(x)
        except ValueError:
            print("Invalid input! Please enter numerical values.")
            continue

        print(f"Result of {op_name}: {result}")

        again = input("Perform another operation? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
