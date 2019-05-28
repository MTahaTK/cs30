# Course: CS 30
# Period: 2
# Date created: 19/03/12
# Date last modified: 19/03/29
# Name: Taha Khokhar
# Description: User-input-based calculator with a square root function
# as a bonus.

import math


def add(x, y):
    """Adds two integers together"""
    sum = f"{x} + {y} = {int(x) + int(y)}"
    return sum


def subtract(x, y):
    """Subtracts two integers"""
    diff = f"{x} - {y} = {int(x) - int(y)}"
    return diff


def mult(x, y):
    """Multiplies two integers together"""
    prod = f"{x} * {y} = {int(x) * int(y)}"
    return prod


def div(x, y):
    """Divides two integers"""
    quotient = f"{x} / {y} = {int(x) / int(y)}"
    return quotient


def longdiv(x, y):
    """Divides two integers and returns its remainder alongside
    the quotient."""
    long_quotient = math.floor(div(x, y))
    remainder = int(x) % int(y)
    longdiv_quotient = f"{x} / {y} = {long_quotient} R{remainder}"
    return longdiv_quotient


def square_list(rad):
    """Creates a list of perfect square factors of a number."""
    squares = []
    i = 2
    while i ** 2 <= rad + 1:
        s = i ** 2
        squares.append(s)
        i += 1
    return squares


def square_root(x):
    """Finds the square root of a single given integer. If the value
    is not a perfect square, the radical is simplified to a mixed
    radical."""
    rad = int(x)
    mods = []
    # Checks whether or not the radical (input) is positive
    if rad >= 0:
        q = int(math.sqrt(rad))
        # Creates a list of all perfect squares less than or equal to
        # the provided number that are greater than 1
        squares = square_list(rad)
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
                    root = f"√{rad} = {sq}√{div}"
                elif 0 not in mods:
                    root = f"√{rad} = √{rad} "
    # If the radical is positive, this takes the absolute value of the
    # radical and runs it through the same operations as the previous
    # branch. The returned 'root' is in terms of i.
    else:
        rad = abs(rad)
        q = int(math.sqrt(rad))
        squares = square_list(rad)
        if len(squares) <= 1:
            root = f"√-{rad} = i√{rad}"
        if rad in squares:
            if q > 1:
                root = f"√-{rad} = {q}i"
            else:
                root = f"√-{rad} = i"
        else:
            for z in squares:
                mod = rad % z
                mods.append(mod)
                if mod == 0:
                    div = int(rad / z)
                    sq = int(math.sqrt(z))
                    root = f"√-{rad} = {sq}i√{div}"
                elif 0 not in mods:
                    root = f"√-{rad} = i√{rad}"
    return root


def inp_quit():
    """Quits program after printing a message."""
    print("-------------------------")
    print("Thank you for using this program.")
    print("I hope you enjoyed using it.")
    exit()


def cont():
    msg = input("Press enter to continue. ")


# Creates a series of prompts for each of the mathematical functions
# defined earlier.
poss = ["1", "2", "3", "4", "5", "6", "quit"]

prompt = """Enter '1' to add two integers.
Enter '2' to subtract two integers.
Enter '3' to multiply two integers.
Enter '4' to divide two integers.
Enter '5' for whole number division with a remainder.
Enter '6' to calculate simplified square roots.
Enter 'quit' to end the program. """

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
        cont()

    # Check for addition operation
    if msg == '1':
        print("-------------------------")
        # First number inputted
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        while act:
            try:
                x = input("Enter the first number: ")
                if x == 'quit':
                    inp_quit()
                # Second number inputted
                y = input("Enter the second number: ")
                if y == 'quit':
                    inp_quit()
                print("-------------------------")
                print(add(x, y))
                cont()
                act = False
            except ValueError:
                print("Please enter integers only.")

    # Check for subtraction operation
    if msg == '2':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request new inputs.
        while act:
            try:
                x = input("Enter the first number: ")
                if x == 'quit':
                    inp_quit()
                y = input("Enter the second number: ")
                if y == 'quit':
                    inp_quit()
                print("-------------------------")
                print(subtract(x, y))
                cont()
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
                x = input("Enter the first number: ")
                if x == 'quit':
                    inp_quit()
                y = input("Enter the second number: ")
                if y == 'quit':
                    inp_quit()
                print("-------------------------")
                print(mult(x, y))
                cont()
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
                x = input("Enter the first number: ")
                if x == 'quit':
                    inp_quit()
                y = input("Enter the second number: ")
                if y == 'quit':
                    inp_quit()
                print("-------------------------")
                print(div(x, y))
                cont()
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
                x = input("Enter the first number: ")
                if x == 'quit':
                    inp_quit()
                y = input("Enter the second number: ")
                if y == 'quit':
                    inp_quit()
                print("-------------------------")
                # If-else statement that checks whether or not the inputs
                # are positive. If they are not, new inputs are requested.
                if int(x) < 0 or int(y) < 0:
                    print("Please input positive integers.")
                else:
                    print(longdiv(x, y))
                    cont()
                    act = False
            except ValueError:
                print("Please input an integer.")
            except ZeroDivisionError as error:
                print(f"{error}: Cannot divide by 0. Please try"
                      " again. ")

    # Check for square root operation
    if msg == '6':
        print("-------------------------")
        act = True
        # While act is true, this branch runs and a try - except statement
        # is evaluated to alert the user of errors and to request a new input.
        while act:
            try:
                x = input("Enter the number you would like to"
                          " find the root of. ")
                if x == 'quit':
                    inp_quit()
                print("-------------------------")
                print(square_root(x))
                cont()
                act = False
            except ValueError:
                print("Please input an integer.")

    # Checks for user input as 'quit.' If the input is 'quit,' the program
    # ends.
    if msg == 'quit':
        inp_quit()
