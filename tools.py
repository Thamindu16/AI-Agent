def add(num1, num2):
    return round(num1 + num2, 2)


def subtract(num1, num2):
    return round(num1 - num2, 2)


def multiply(num1, num2):
    return round(num1 * num2, 2)


def divide(num1, num2):

    if num2 == 0:
        return "Cannot divide by zero"

    return round(num1 / num2, 2)