'''
Functions banawnu sike, ani exception handling pani sike.
noice
'''
def sum(num1, num2):
    return num1 + num2


def difference(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
       return num1 / num2


try:
    firstNumber = int(input("Enter num1: "))
    secondNumber = int(input("Enter num2: "))
    print(sum(firstNumber, secondNumber))
    print(difference(firstNumber, secondNumber))
    print(multiply(firstNumber, secondNumber))
    try:
        print((divide(firstNumber, secondNumber)))
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
        print("value cannot be null")