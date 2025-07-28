# project calculator
print("CALCULATOR")
print(" ")
print("Enter the method:")
method = input()
print(" ")
print("Enter the first number:")
first_number = input()
print("Enter the second number:")
second_number = input()

if int(method) == 1:
    print("You have chosen ADD:")
    print(" ")
    Sum = int(first_number) + int(second_number)
    print(Sum)

elif int(method) == 2:
    print("You have chosen SUBTRACT:")
    print(" ")
    Subtract = int(first_number) - int(second_number)
    print(Subtract)

elif int(method) == 3:
    print("You have chosen MULTIPLY:")
    print(" ")
    Multiply = int(first_number) * int(second_number)
    print(Multiply)

elif int(method) == 4:
    print("You have chosen DIVIDE:")
    print(" ")
    if int(second_number) == 0:
        print("Error: Cannot divide by zero.")
    else:
        Divide = int(first_number) / int(second_number)
        print(Divide)

else:
    print("Invalid Method Selection")

print("*******Thanks for using Calculator********")
