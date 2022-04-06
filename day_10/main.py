# start to python day-10 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 28-03-2022
# went on vacation
import math

# def format_name(first_name, last_name):
#     if first_name == "" or last_name == "":
#         return "You didn't provide valid inputs"
#     f_first_name = first_name.title()
#     f_last_name = last_name.title()
#     return (f_first_name +" "+ f_last_name)
#
# print(format_name(input("What is your f_name: "), input("What is your l_name: ")))

# Calculator

def add(n1, n2):
    """Addition function"""
    return n1 + n2


def subtract(n1, n2):
    """Subtraction function"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplication function"""
    return n1 * n2


def divide(n1, n2):
    """Divide function"""
    return n1 / n2

# created the dictionary with symbol as key and its function as value
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calc():
    num1 = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = False

    while not should_continue:

        operations_symbol = input("Pick an operation: ")
        num2 = float(input("Enter next number: "))

        # for calculation taking function from dict
        calculation_function = operations[operations_symbol]
        #calling the function as selected by user
        answer = calculation_function(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' for new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = True
            calc()
    # operations_symbol = input("Pick another operation: ")
    # num3 = int(input("Enter next number: "))
    # # for calculation taking function from dict
    # calculation_function = operations[operations_symbol]
    # #calling the function as selected by user
    # second_answer = calculation_function(answer, num3)
    #
    # print(f"{answer} {operations_symbol} {num3} = {second_answer}")
    #

calc()