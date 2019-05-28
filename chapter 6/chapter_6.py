# 6-1
person_data = {'first_name': 'taha', 'last_name': 'khokhar', 'age': 17}

print(f"This person's first name is {person_data['first_name'].title()}.")
print(f"This person's last name is {person_data['last_name'].title()}.")
print(f"This person is {person_data['age']} years old.")

# 6-2
fav_num = {
    'taha': 15,
    'haris': 3,
    'andrew': -10,
    }

for n, num in fav_num.items():
    print(f"{n.title()}'s favourite number is {num}.")

# 6-3
glos = {
    'halide': 'Binary compound containing a halogen.',
    'monk': 'Andrew Li.',
    'lone pair': 'Pairs of electrons attracted to atoms with an ' +
    'unfulfilled octet valence shell.',
    'a': 'First letter of the alphabet',
    'b': 'Second letter of the alphabet',
    'z': 'Twenty-sixth letter of the alphabet',
    'c': 'Third letter of the alphabet',
    'sad': 'me',
}

keys = [x for x in glos.keys()]
keys.sort()print(keys)
for word in sorted(keys):
    for w, d in glos.items():
        if w == word:
            print(f"{w.title()}: {d}")
