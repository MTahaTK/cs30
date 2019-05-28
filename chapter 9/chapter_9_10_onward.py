# 9-10
print("\n9-10")
from restaurant import Restaurant

biggo = Restaurant("nammsssd", "frenchhhh")
biggo.describe_restaurant()

# 9-11
print("\n9-11")
from users import Admin

admin = Admin('taha', 'khokhar',)

admin.describe_user()

admin.privileges.privileges = [
    'can reset',
    'can annihilate',
    'absolute control'
]


admin.privileges.show_privileges()

# 9-12
print("9-12 is in a separate file.")

# 9-13
print("\n9-12")

from collections import OrderedDict

word = OrderedDict()

word['a'] = 'First letter of the alphabet'
word['b'] = 'Second letter of the alphabet'
word['c'] = 'Third letter of the alphabet'
word['halide'] = 'Binary compound containing a halogen.'
word['lone pair'] = ('Pairs of electrons attracted to atoms with an ' +
                     'unfulfilled octet valence shell.')
word['monk'] = 'Andrew Li.'
word['sad'] = 'me'
word['z'] = 'Twenty-sixth letter of the alphabet'

for w, defi in word.items():
    print(f"{w.title()}: {defi}")

# 9-14
print("\n9-14")

from random import randint

class Die:
    """Represents a rollable die"""
    def __init__(self, sides=6):
        """Initializes die"""
        self.sides = sides

    def roll_die(self):
        """Rolls dice based on sides and random chance"""
        return randint(1, self.sides)

six_sided = Die(6)

n = 0
print("\n-----------SIX-SIDED-----------")
while n < 10:
    print(six_sided.roll_die())
    n += 1

dodeca = Die(10)

x = 0
print("\n-----------TEN-SIDED-----------")
while x < 10:
    print(dodeca.roll_die())
    x += 1

twenty = Die(20)

i = 0
print("\n-----------TWENTY-SIDED-----------")
while i < 10:
    print(twenty.roll_die())
    i += 1
