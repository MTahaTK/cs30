# Course: CS 30
# Period: 2
# Date created: 19/04/07
# Date last modified: 19/04/18
# Name: Taha Khokhar
# Description: User-input-based text game. It should be noted that this game
# pays homage and may be taken as an adaptation of the game Bloodborne by
# FromSoftware.

from khokhar_taha_objects import *


def equip_weapon():
    """Defines equip weapon function"""
    while True:
        print(f"In your inventory you have the following weapons: "
              f"{str(player.inventory)}")
        # Stores weapon request from an input into a variable
        wep_req = input('What weapon would you like to equip?\n')
        wep_req = wep_req.title()
        # Checks if the requested weapon is in the user's inventory
        if wep_req in player.inventory:
            player.equipped_wep = wep_req
            return(f"You have equipped the {wep_req}.")
            break
        else:
            print(f"You do not possess this weapon.")


def attack(inp):
    """Defines the attacking/combat function and event"""
    while True:
        if inp == player.name:
            return "You cannot attack yourself."
            break
        # Checks to see if inputted object is valid (not a weapon name or
        # player name)
        elif (inp in GameObject.objects and inp != player.name and
              GameObject.objects[inp].class_name != 'weapon'):
            if GameObject.objects[inp].health <= 0:
                return "You have already slain your opponent."
                break
            while True:
                # Gives player choice between light and heavy attacks
                attack_type = input("What kind of attack would you like to "
                                    "use? (Light/Heavy): ").title()
                # Determines damage output based on type of attack and weapon
                # equipped and stores in damage variable
                if player.equipped_wep == '':
                    if attack_type == 'Light':
                        damage = player.strength
                        break
                    elif attack_type == 'Heavy':
                        damage = 2.5 * player.strength
                        break
                else:
                    if attack_type == 'Light':
                        damage = GameObject.objects[player.equipped_wep].dam
                        break
                    elif attack_type == 'Heavy':
                        damage = GameObject.objects[player.equipped_wep].dam
                        damage = 2.5 * damage
                        break
            # Subtracts damage from enemy health and damage is dealth by the
            # enemy to the player, whose health is then calculated and
            # outputted. If the player's health reaches 0, the game ends. The
            # ending condition is processed in another function.
            while True:
                GameObject.objects[inp].health -= damage
                if GameObject.objects[inp].health < 0:
                    GameObject.objects[inp].health = 0
                print(f"Hit successful. Damage dealt: {damage}.\nEnemy"
                      f" Health: {int(GameObject.objects[inp].health)}.")
                if GameObject.objects[inp].health == 0:
                    return (f"You have slain your enemy.")
                    break
                enemy_damage = GameObject.objects[inp].enemy_dam
                if player.health < 0:
                    player.health = 0
                if player.health <= 0:
                    return f"Health: {int(player.health)}.\nYou Died."
                    break
                player.health -= enemy_damage
                if player.health < 0:
                    player.health = 0
                if player.health <= 0:
                    return f"Health: {int(player.health)}.\nYou Died."
                    break
                return(f"Your opponent strikes you. Damage taken: "
                       f"{enemy_damage}.\nYour health: {int(player.health)}")
        else:
            return f"Unknown enemy '{inp}'. Please enter a valid enemy name."
            break


def heal():
    """Defines healing function"""
    while True:
        # Checks if player actually has health potions - or blood vials - in
        # their inventory
        if player.health_pot == 0:
            return "You have no blood vials to heal with."
            break
        else:
            print(f"You have {player.health_pot} blood vials.")
            # Requests confirmation for healing
            conf = input("Would you like to heal using a blood vial?"
                         "(Yes/No)\n").title()
            # Determines whether or not player is at maximum health. If not,
            # the player is healed.
            if conf == "Yes":
                if player.health >= 10 * player.vit:
                    return "You are already at maximum health"
                    break
                else:
                    player.health_pot -= 1
                    player.health += 0.4 * (10 * player.vit)
                    if player.health >= 10 * player.vit:
                        player.health = 10 * player.vit
                    return(f"You now have {int(player.health)} health "
                           "points.")
                    break
            elif conf == "No":
                return "Healing cancelled."
                break


def get_input():
    """Defines inputting function"""
    while True:
        # Simple method for losing condition by placing this line of code in
        # the function that essentially runs the game rather than individual
        # functions.
        if player.health <= 0:
            break
        # Requests input from player and processes the input based on whether
        # or not the given keyword matches a key in the action word dictionary
        command = input("What would you like to do?: ").split()
        act_command = command[0]
        if act_command in act_dict:
            action = act_dict[act_command]
        # Quits game based on 'quit' input.
        elif act_command == 'quit':
            print("Thank you for playing.\nExiting game....")
            break
        else:
            print(f"Unknown command '{act_command}.' Please enter a valid"
                  " command out of those in the action dictionary.")
            continue
        # Since the 'attack' command requires a target for the attack, this
        # ensures that there is a second argument provided that acts as a
        # target. If there is a valid second argument, all words that come
        # after the intial verb are converted into a string to be compared to
        # the defined enemy/NPC classes
        if act_command == "attack":
            if len(command) < 2:
                print("Please provide your target for this action.")
            if len(command) >= 2:
                target_str = ' '.join(command[1:]).title()
                print(action(target_str))
        else:
            print(action())

# Action word dictionary
act_dict = {"heal": heal, "attack": attack, "equip": equip_weapon}

# Assembling all NPCs and weapons and placing them in user's inventory (had
# planned to make an exploration system that allowed for one to find and
# pick up weapons, but had to simplify this to this sort of system).
enemy = Lycanthrope("Lycanthrope")
brokensword = BrokenSword('Broken Sword')
flailsaw = FlailSaw('Flailsaw')
bom = BOM('Blade of Mercy')
elbow = ElbowBlade('Piercing Wing')
smashfist = SmashFist('Infernal Sledges')
player = Player('Hunter')
player.inventory_class = [brokensword]
player.inventory = [brokensword.name]
player.inventory_class += [flailsaw]
player.inventory += [flailsaw.name]
player.inventory_class += [bom]
player.inventory += [bom.name]
player.inventory_class += [elbow]
player.inventory += [elbow.name]
player.inventory_class += [smashfist]
player.inventory += [smashfist.name]

# Game is run
print("Welcome to BB_Text!")
print("As you awaken, you stumble forward to find yourself face to face with "
      "a lycanthrope.")
get_input()
