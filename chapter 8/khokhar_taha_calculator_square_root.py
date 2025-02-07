# Course: CS 30
# Period: 2
# Date created: 19/03/12
# Date last modified: 19/03/25
# Name: Taha Khokhar
# Description: User-input-based calculator with a square root function
# as a bonus.

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


def square_root(x):
    """Finds the square root of a single given integer. If the value
    is not a perfect square, the radical is simplified to a mixed
    radical."""
    rad = int(x)
    squares = []
    mods = []
    # Checks whether or not the radical (input) is positive
    if rad >= 0:
        i = 2
        q = int(math.sqrt(rad))
        # Creates a list of all perfect squares less than or equal to
        # the provided number that are greater than 1
        while i ** 2 <= rad + 1:
            s = i ** 2
            squares.append(s)
            i += 1
        if len(squares) <= 1:
            root = f"√{rad}"
        if rad in squares:
            root = f"{q}"
        else:
            # Loops through values of z, then mods rad by z. This then
            # creates a list of mods.
            for z in squares:
                mod = rad % z
                mods.append(mod)
                # Based on the order the mods list is formed in, the
                # greatest values for mod of 0 come first. As such,
                # this checks for the first instance of a mod of ,
                # then simplifies the square.
                if mod == 0:
                    div = int(rad / z)
                    sq = int(math.sqrt(z))
                    root = f"{sq}√{div}"
                elif 0 not in mods:
                    root = f"√{rad}"
    # If the radical is positive, this takes the absolute value of the
    # radical and runs it through the same operations as the previous
    # branch. The returned 'root' is in terms of i.
    else:
        rad = abs(rad)
        i = 2
        q = int(math.sqrt(rad))
        while i ** 2 <= rad + 1:
            s = i ** 2
            squares.append(s)
            i += 1
        if len(squares) <= 1:
            root = f"i√{rad}"
        if rad in squares:
            if q > 1:
                root = f"{q}i"
            else:
                root = f"i"
        else:
            for z in squares:
                mod = rad % z
                mods.append(mod)
                if mod == 0:
                    div = int(rad / z)
                    sq = int(math.sqrt(z))
                    root = f"{sq}i√{div}"
                elif 0 not in mods:
                    root = f"i√{rad}"
    return root

# Creates a series of prompts for each of the mathematical functions
# defined earlier.
poss = ["1", "2", "3", "4", "5", "6", "quit"]

prompt = "Enter '1' to add two integers. "
prompt += "\nEnter '2' to subtract two integers. "
prompt += "\nEnter '3' to multiply two integers. "
prompt += "\nEnter '4' to divide two integers. "
prompt += "\nEnter '5' for whole number division with a remainder. "
prompt += "\nEnter '6' to calculate simplified square roots. "
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

    # Checks whether or not the input is a valid input
    if msg not in poss:
        print("-------------------------")
        print("Please provide a valid input.")
        msg = input("Enter anything to continue. ")

    # Check for addition operation
    if msg == '1':
        print("-------------------------")
        # First number inputted
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        while act:
            try:
                x = input("Enter the first number. ")
                if x == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                # Second number inputted
                y = input("Enter the second number. ")
                if y == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                print("-------------------------")
                print(f"{x} + {y} = {add(x, y)}")
                msg = input("Enter anything to continue. ")
                act = False
            except ValueError:
                print("Please enter an integer.")

    # Check for subtraction operation
    if msg == '2':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        while act:
            try:
                x = input("Enter the first number. ")
                if x == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                y = input("Enter the second number. ")
                if y == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                print("-------------------------")
                print(f"{x} - {y} = {subtract(x, y)}")
                msg = input("Enter anything to continue. ")
                act = False
            except ValueError:
                print("Please enter an integer.")

    # Check for multiplication operation
    if msg == '3':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        while act:
            try:
                x = input("Enter the first number. ")
                if x == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                y = input("Enter the second number. ")
                if y == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                print("-------------------------")
                print(f"{x} * {y} = {mult(x, y)}")
                msg = input("Enter anything to continue. ")
                act = False
            except ValueError:
                print("Please enter an integer.")

    # Check for division operation
    if msg == '4':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        # This one also has a branch for any ZeroDivisionErrors that arise.
        while act:
            try:
                x = input("Enter the first number. ")
                if x == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                y = input("Enter the second number. ")
                if y == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                print("-------------------------")
                print(f"{x} / {y} = {div(x, y)}")
                msg = input("Enter anything to continue. ")
                act = False
            except ValueError:
                print("Please input an integer.")
            except ZeroDivisionError as error:
                print(f"{error}: Cannot divide by 0.")

    # Check for long division operation
    if msg == '5':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        # This one also has a branch for any ZeroDivisionErrors that arise.
        while act:
            try:
                x = input("Enter the first number. ")
                if x == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                y = input("Enter the second number. ")
                if y == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                print("-------------------------")
                # If-else statement that checks whether or not the inputs
                # are positive. If they are not, new inputs are requested.
                if int(x) < 0 or int(y) < 0:
                    print("Please input positive integers.")
                else:
                    print(f"{x} / {y} = {longdiv(x, y)}")
                    msg = input("Enter anything to continue. ")
                    act = False
            except ValueError:
                print("Please input an integer.")
            except ZeroDivisionError as error:
                print(f"{error}: Cannot divide by 0.")

    # Check for square root operation
    if msg == '6':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request a new input.
        while act:
            try:
                x = input("Enter the number you would like to find the root of. ")
                if x == 'quit':
                    print("-------------------------")
                    print("Thank you for using this program.")
                    print("I hope you enjoyed using it.")
                    active = False
                    break
                print("-------------------------")
                print(f"√{x} = {square_root(x)}")
                msg = input("Enter anything to continue. ")
                act = False
            except ValueError:
                print("Please input an integer.")

    # Checks for user input as 'quit.' If the input is 'quit,' the program
    # ends.    
    if msg == 'quit':
        print("-------------------------")
        print("Thank you for using this program.")
        print("I hope you enjoyed using it.")
        active = False
        act = False
