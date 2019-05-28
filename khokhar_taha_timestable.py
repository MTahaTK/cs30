# Course: CS 30
# Period: 2
# Date created: 19/02/09
# Date last modified: 19/02/11
# Name: Taha Khokhar
# Description: Runs through a range from 0 to 12 and prints a list of that
# value's time table up to the 12 times table.


x = int(input())
table = x + 1
# Defines a list num as a range from 0 to 12.
num = list(range(0, table))

# Starts a for loop that repeats the contained expression for values
# from 0 to 12, where the value of z in the list comprehension prod is
# multiplied by num[i]. Prod is then printed for each value of i.
for i in range(0, table):
    prod = [z*num[i] for z in range(0, table)]
    print(prod)
