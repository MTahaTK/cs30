# 5-3 - Alternate
colours = ['green', 'yellow', 'red',]
point_val = {'green': 1, 'yellow': 2, 'red': 5}

import random
alien_colour = colours[random.randint(0,2)]
print(alien_colour)

if alien_colour == colours[0]:
    print(f"{point_val[alien_colour]} point.")
elif alien_colour == colours[1]:
    print(f"{point_val[alien_colour]} points.")
elif alien_colour == colours[2]:
    print(f"{point_val[alien_colour]} points.")

# 5-3
print("\n5-3")
alien_colour = 'green'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")

alien_colour = 'red'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")

# 5-4
print("\n5-4")
alien_colour = 'green'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")
else:
    print("10 points awarded.")

alien_colour = 'red'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")
else:
    print("10 points awarded.")

# 5-5
print("\n5-5")
alien_colour = 'green'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")
elif alien_colour == 'yellow':
    print("Yellow eliminated. 10 points awarded.")
else:
    print("Red eliminated. 15 points awarded.")

alien_colour = 'yellow'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")
elif alien_colour == 'yellow':
    print("Yellow eliminated. 10 points awarded.")
else:
    print("Red eliminated. 15 points awarded.")

alien_colour = 'red'

if alien_colour == 'green':
    print("Green eliminated. 5 points awarded.")
elif alien_colour == 'yellow':
    print("Yellow eliminated. 10 points awarded.")
else:
    print("Red eliminated. 15 points awarded.")

# 5-6
print("\n5-6")
age = float(input("How old are you?"))

if age < 2:
    print("You must be a baby/infant.")
elif age >= 2 and age < 4:
    print("You must be a toddler.")
elif age >= 4 and age < 13:
    print("You must be a kid/child.")
elif age >= 13 and age < 20:
    print("You must be a teenager.")
elif age >= 20 and age < 65:
    print("You must be an adult.")
else:
    print("You must be an elder.")
