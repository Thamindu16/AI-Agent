def add():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    return round(num1 + num2, 2)


def subtract():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    return round(num1 - num2, 2)


def multiply():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    return round(num1 * num2, 2)


def divide():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num2 == 0:
        return "Cannot divide by zero"

    return round(num1 / num2, 2)