class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

class AdvancedCalculator(Calculator):
    def power(self, x, y):
        return x ** y

def main():
    calc = AdvancedCalculator()
    operations = {
        '1': ('Addition', calc.add),
        '2': ('Subtraction', calc.subtract),
        '3': ('Multiplication', calc.multiply),
        '4': ('Division', calc.divide),
        '5': ('Power', calc.power)
    }
    while True:
        print("\nChoose operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        op_name, func = operations[choice]
        result = func(x, y)
        print(f"Result of {op_name}: {result}")
        again = input("Do you want to perform another operation? (y/n): ")
        if again.lower() != 'y':
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    main()