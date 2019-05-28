# Course: CS 30
# Period: 2
# Date created: 19/02/07
# Date last modified: 19/02/26
# Name: Taha Khokhar
# Description: Various interactions and operations upon a list
# of weapons from
# the game Bloodborne

# This organizes a collection of the items I found off of a
# website into a
# single string and dumps it into the variable foo.
foo = """Hunter Pistol
Hunter Blunderbuss
Torch
Repeating Pistol
Wooden Shield
Flamesprayer
Hunter's Torch
Ludwig's Rifle
Evelyn
Rosmarinus
Blade of Mercy
Saw Cleaver
Saw Spear
Hunter Axe
Threaded Cane
Kirkhammer
Rifle Spear
Stake Driver
Ludwig's Holy Blade
Cannon
Tonitrus
Reiterpallasch
Chikage
Logarius Wheel
Beast Claw
Burial Blade
Amygdalan Arm
Beasthunter Saif
Beast Cutter
Bloodletter
Boom Hammer
Church Pick
Holy Moonlight Sword
Kos Parasite
Rakuyo
Simon's Bowblade
Whirligig Saw
Church Cannon
Fist of Gratia
Gatling Gun
Piercing Rifle
Loch Shield
"""
# Splits the variable foo containing a string of the aforementioned weapons
# into a list.
weps = foo.splitlines()

# Counts the number of elements in the list weps
wep_num = len(weps)

# Prints message containing the variable wep_num
print("Throughout the entirety of Bloodborne, there are " +
      f"{wep_num} weapons in total.")

# Appends the value of weps[0] into the list base_weps, then
# deletes this value, subsequently incrementing i by 1. This loop
# continues until i is less than or equal to 25.
base_weps = []
i = 0
while i <= 25:
    base_weps.append(weps[0])
    del weps[0]
    i += 1

# Stores length of the newly created base_weps and the length of
# weps after removing all of the elements in base_weps from it
# into variables.
base_weps_num = len(base_weps)
dlc_weps_num = len(weps)

# Prints messages concerning information on the base_weps list.
print(f"There are {base_weps_num} weapons available in the base " +
      "game of Bloodborne.")
print("In alphabetical order, they are as follows: " +
      f"{sorted(base_weps)}")

# Prints messages concerning information on the new weps list.
print("In the 'Old Hunters' DLC for Bloodborne, there are a total" +
      f" of {dlc_weps_num} weapons added into the game.")
print("In alphabetical order, they are as follows: " +
      f"{sorted(weps)}")

# Reverses weps variable to append values onto the end of it.
weps.reverse()

# Essentially undoes the previous while loop by appending the
# value of base_weps[0] into weps (after reversing it), then
# it removes this value from base_weps. This continues as long
# as i is less than or equal to 25. It is incremented by 1 in
# each loop.
i = 0
while i <= 25:
    weps.append(base_weps[0])
    del base_weps[0]
    i += 1

# Reverses weps back to its original order.
weps.reverse()

# Prints statement concerning the new weps list.
print("Therefore, the complete list of weapons in Bloodborne is " +
      f"as follows: {sorted(weps)}")

# Since the exact elements to be placed in the newly defined
# offhand list are known, this inserts these known elements into
# the 0 position of offhand one after the other
offhand = []
offhand.insert(0, 'Reiterpallasch')
offhand.insert(0, 'Cannon')
offhand.insert(0, 'Rosmarinus')
offhand.insert(0, 'Evelyn')
offhand.insert(0, "Ludwig's Rifle")
offhand.insert(0, "Hunter's Torch")
offhand.insert(0, 'Flamesprayer')
offhand.insert(0, 'Wooden Shield')
offhand.insert(0, 'Repeating Pistol')
offhand.insert(0, 'Torch')
offhand.insert(0, 'Hunter Blunderbuss')
offhand.insert(0, 'Hunter Pistol')
offhand.insert(0, 'Church Cannon')
offhand.insert(0, 'Fist of Gratia')
offhand.insert(0, 'Gatling Gun')
offhand.insert(0, 'Piercing Rifle')
offhand.insert(0, 'Loch Shield')

# Sorts the offhand list
offhand.sort()

# Prints statement concerning the list offhand.
print("The list of sidearms, or off-hand weapons, throughout the" +
      f" entirety of the game is as follows: {offhand}")

# Removes all of the elements added into offhand from weps
weps.remove('Reiterpallasch')
weps.remove('Cannon')
weps.remove('Rosmarinus')
weps.remove('Evelyn')
weps.remove("Ludwig's Rifle")
weps.remove("Hunter's Torch")
weps.remove('Flamesprayer')
weps.remove('Wooden Shield')
weps.remove('Repeating Pistol')
weps.remove('Torch')
weps.remove('Hunter Blunderbuss')
weps.remove('Hunter Pistol')
weps.remove('Church Cannon')
weps.remove('Fist of Gratia')
weps.remove('Gatling Gun')
weps.remove('Piercing Rifle')
weps.remove('Loch Shield')

# Sorts the weps list after removing all of the offhand weapons
weps.sort()

# Prints statement concerning the weps list after removing all
# sidearms from the list
print("As such, the primary or main-hand weapons in Bloodborne " +
      f"are as follows: {weps}")

# Uses the pop function and known indices to place specific
# elements from weps into fav_main and from offhand to
# fav_offhand respectively
fav_main = weps.pop(18)
fav_offhand = offhand.pop(6)

# Prints out statement concerning favourite weapons
print("My favourite weapons out of all of these, however, are " +
      f"the {fav_main} as my main-hand weapon and the " +
      f"{fav_offhand} as my sidearm.")
