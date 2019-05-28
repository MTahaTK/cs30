# Course: CS 30
# Period: 2
# Date created: 19/03/12
# Date last modified: 19/03/13
# Name: Taha Khokhar
# Description: User-input-based calculator

import math


def add(x, y):
    """Adds two integers together"""
    sum = int(x) + int(y)
    return sum


def subtract(x, y):
    """Subtracts two integers"""
    diff = int(x) - int(y)
    return diff


def mult(x, y):
    """Multiplies two integers together"""
    prod = int(x) * int(y)
    return prod


def div(x, y):
    """Divides two integers"""
    quotient = int(x) / int(y)
    return quotient


def longdiv(x, y):
    """Divides two integers and returns its remainder alongside
    the quotient."""
    long_quotient = math.floor(div(x, y))
    remainder = int(x) % int(y)
    longdiv_quotient = f"{long_quotient} R{remainder}"
    return longdiv_quotient

# Creates a series of prompts for each of the mathematical functions
# defined earlier.
prompt = "Enter '1' to add two integers. "
prompt += "\nEnter '2' to subtract two integers. "
prompt += "\nEnter '3' to multiply two integers. "
prompt += "\nEnter '4' to divide two integers. "
prompt += "\nEnter '5' for whole number division with a remainder. "
prompt += "\nEnter 'quit' to end the program. "

# Sets a flag - active - as True.
active = True

# Loops through if statements that check the given input for the
# program. The if statements will run the respective mathematical
# functions for each provided input. Then, the result of each function
# is printed out and the prompts appear once again. The last if
# statement quits the program if 'quit' is inputted. For each operation
# branch, the program checks whether or not the provided inputs for
# the terms are 'quit.' If they are, the program quits.
while active:
    print("-------------------------")
    msg = input(prompt)
    if msg == '1':
        print("-------------------------")
        # First number input
        x = input("Enter the first number. ")
        if x == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        # Second number input
        y = input("Enter the second number. ")
        if y == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        print("-------------------------")
        print(f"{x} + {y} = {add(x, y)}")
        msg = input("Enter anything to continue. ")

    if msg == '2':
        print("-------------------------")
        x = input("Enter the first number. ")
        if x == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        y = input("Enter the second number. ")
        if y == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        print("-------------------------")
        print(f"{x} - {y} = {subtract(x, y)}")
        msg = input("Enter anything to continue. ")

    if msg == '3':
        print("-------------------------")
        x = input("Enter the first number. ")
        if x == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        y = input("Enter the second number. ")
        if y == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        print("-------------------------")
        print(f"{x} * {y} = {mult(x, y)}")
        msg = input("Enter anything to continue. ")

    if msg == '4':
        print("-------------------------")
        x = input("Enter the first number. ")
        if x == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        y = input("Enter the second number. ")
        if y == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        print("-------------------------")
        print(f"{x} / {y} = {div(x, y)}")
        msg = input("Enter anything to continue. ")

    if msg == '5':
        print("-------------------------")
        x = input("Enter the first number. ")
        if x == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        y = input("Enter the second number. ")
        if y == 'quit':
            print("-------------------------")
            print("Thank you for using this program.")
            print("I hope you enjoyed using it.")
            break
        print("-------------------------")
        print(f"{x} / {y} = {longdiv(x, y)}")
        msg = input("Enter anything to continue. ")

    if msg == 'quit':
        print("-------------------------")
        print("Thank you for using this program.")
        print("I hope you enjoyed using it.")
        active = False
