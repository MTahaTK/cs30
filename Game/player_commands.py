import random

from game_wip import *


def equip_weapon():
    print(player.inventory)
    while True:
        wep_req = input('What weapon would you like to equip?\n')
        wep_req = wep_req.title()
        if wep_req in player.inventory:
            player.equipped_wep = wep_req
            print(f"You have equipped the {wep_req}.")
            break
        else:
            print(f"You do not possess this weapon.")


def attack(inp):
    while True:
        if inp == player.name:
            return "You cannot attack yourself."
            break
        elif (inp in GameObject.objects and inp != player.name and
            GameObject.objects[inp].class_name != 'weapon'):
            if GameObject.objects[inp].health <= 0:
                 return "You have already slain your opponent."
                 break
            else:
                while True:
                    if player.equipped_wep == '':
                        damage = player.strength
                        break
                    else:
                        damage = GameObject.objects[player.equipped_wep].dam
                        break
            enemy.health -= damage
            return (f"Your attack upon the {inp.title()} dealt {damage} points"
                    f" of damage. The {inp.title()} now has {enemy.health}"
                    " health points.")

def heal():
    while True:
        if player.health_pot == 0:
            print("You have no blood vials to heal with.")
            break
        else:
            print(f"You have {player.health_pot} blood vials.")
            conf = input("Would you like to heal using a blood vial?"
                        "(Yes/No)\n")
            if conf == "Yes":
                if player.health == 10 * player.vit:
                    print("You are already at maximum health")
                    break
                else:
                    player.health += 0.4 * (10 * player.vit)
                    print(f"You now have {player.health} health points.")
                    break
            elif conf == "No":
                print("Healing cancelled.")
                break

def get_input():
    while True:
        command = input("What would you like to do?: ").split()
        act_command = command[0]
        if act_command in act_dict:
            action = act_dict[act_command]
        elif act_command == 'quit':
            print("Thank you for playing\nExiting game....")
            break
        else:
            print(f"Unknown command '{act_command}.' Please enter a valid"
                 " command out of those in the action dictionary.")
            continue

        if act_command == "attack":
            if len(command) < 2:
                print("Please provide your target for this action.")
            if len(command) >= 2:
                print(command[1:])
                # target = command[1].title()
                #
                # print(action(target))
        else:
            action()



act_dict = {"heal": heal, "attack": attack, "equip": equip_weapon}



enemy = Enemy("Huntsman")
brokensword = BrokenSword('Broken Sword')

player = Player('Hunter')
player.inventory_class = [brokensword]
player.inventory = [brokensword.name]
print(player.inventory)
print(player.inventory_class)
print(player.inventory_class[0].dam)
print(player.equipped_wep)
# player.inventory = ['BrokenSword']
# print(player.inventory)
#
# print(GameObject.objects)
# equip_weapon()
# # print(GameObject.objects[player.equipped_wep].dam)
# attack('Huntsman')
# attack('Huntsman')
#
# attack('Huntsman')
#
get_input()
