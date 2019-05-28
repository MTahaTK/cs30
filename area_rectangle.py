# Course: CS 30
# Period: 1
# Date created: 19/02/03
# Date last modified: 19/02/04
# Name: Janice Cotcher
# Description: Area of a rectangle calculator


def area_rect(l, w):
    """Calculate the area of a rectangle"""
    a = l * w
    return a


# Ask for the user to input an integer value for the length and width of a
# rectangle and print the area.
print("Calculate the area of a rectangle in cm^2:")
length = int(input("What is the length of the rectangle in cm? "))
width = int(input("What is the width of the rectangle in cm? "))
print("The area of the rectangle is " + str(area_rect(length, width)) + "cm^2")
