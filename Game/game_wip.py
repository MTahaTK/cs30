x = "---------------------------------"

class GameObject:
    class_name = ""
    level = 4
    vit = 10
    health = 10 * vit
    strength = 10
    skill = 10
    end = 5
    stam = end * 10
    agi = 10
    gen = ''
    desc = ''
    curr = 0
    health_pot = 20
    inventory_class = []
    inventory = []
    equipped_wep = ''
    objects = {}

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.name] = self

    def get_desc(self):
        return (f"{x}\n{self.name.title()}\nClass: "
                 f"{self.class_name.title()}\nLevel: {self.level}\n"
                 f"Vitality: {self.vit}\nStamina: {self.stam}\nStrength: "
                 f"{self.strength}\nSkill: {self.skill}\nEndurance: "
                 f"{self.end}\nAgility: {self.agi}\nGender: "
                 f"{self.gen.title()}\nMoney: {self.curr}\nInventory: "
                 f"{str(self.inventory)}\nDescription: {self.desc}\n")

class Player(GameObject):
    class_name = "Player"
    curr = 100
    desc = (
    """
    You are a a foreigner to the sprawling city of Yharnam. Your arrival in the
    city bade you as a hunter, and you now seek to end the beastly - and
    potentially eldritch - threat that looms upon it evermore. The dream
    flourishes once more.
    """)

class Enemy(GameObject):
    class_name = "Enemy"
    curr = 100
    desc = (
    """
    You are a a foreigner to the sprawling city of Yharnam. Your arrival in the
    city bade you as a hunter, and you now seek to end the beastly - and
    potentially eldritch - threat that looms upon it evermore. The dream
    flourishes once more.
    """)

# player = Player('hunter')
# print(player.get_desc())


class Weapons(GameObject):
    class_name = 'weapon'
    str_req = 10
    skill_req = 10
    stam_drain = 10
    desc = ''

    def get_desc(self):
        return (f"{x}\n{self.name.title()}\nClass: "
                f"{self.class_name.title()}\nStrength "
                f"Requirement: {self.str_req}\nSkill Requirement: "
                f"{self.skill_req}\nStamina Drain: {self.stam_drain}\n"
                f"{self.desc}")

class BrokenSword(Weapons):
    str_req = 5
    skill_req = 1
    dam = 0.8 * Player.strength + 0.25 * Player.skill
    stam_drain = 5
    desc = (
    """
    A dull, rusted, and broken shortsword. Ineffective as both a
    piercing tool and as a club. Its blunt edge can part flesh with
    some effort, however.
    """)

# print(BrokenSword('broken sword').get_desc())


class FlailSaw(Weapons):
    str_req = 7
    skill_req = 12
    dam = Player.skill * 1.1 + Player.strength * 0.2
    stam_drain = 7
    desc = (
    """
    A strangely heretical weapon of the forsaken Hunter's Workshop. A physical
    combination of two of the Workshop's most imposing weapons, the Flail Saw
    is, at first, two jagged saw blades attached back-to-back on a long cane
    handle. However, its transformation heralds it as a barbed whip connected
    to a whirring set of blades that cleave enemies with no hint of elegance
    whatsoever.
    """
    )

# print(FlailSaw('flail saw').get_desc())

class BOM(Weapons):
    str_req = 5
    skill_req = 15
    dam = 2 * Player.skill + 0.1 * Player.strength
    stam_drain = 3
    desc = (
    """
    One of the oldest Workshop Trick Weapons in existence. Passed down from
    subsequent Hunters of Hunters, its dagger-like gleaming siderite blade
    splits into two blades of blinding speed.

    The last Hunter of Hunters before the fall of the Healing Church and
    the dream was Eileen the Crow. Her dedication to the cause led to her
    demise by the hand of a special brand of Cainhurst Knight.

    The crow feathers embedded into the handle tell of the betrayal that lost
    this blade to the ages.
    """
    )

# print(BOM('blade of mercy').get_desc())

class ElbowBlade(Weapons):
    str_req = 14
    skill_req = 10
    dam = 1.5 * (Player.strength + Player.skill)
    desc = (
    """
    By far, the Piercing Wing is the most recognizable of all New Workshop
    trick weapons. It consists of two portions: a set of jagged claws and a
    pair of long blades that mount onto one's elbows and transform from a
    further augmentation of the main set of claws to blades that extend upwards
    from the elbows.

    The usage of this weapon requires a remarkable balance of dexterity and raw
    power in combination with the bestial desire to rip one's foes apart. The
    orientation of the blades allow one to first pierce their enemy with the
    claws and forward-facing sword blades, which may lead one into transforming
    the weapon to brutally dismember their foe.

    The Piercing Wing represents a departure from Gehrman's style of trick
    weapons that emphasized one's humanity over their bestial enemies, and
    rather embraces the bloodlust that comes with the hunt.
    """
    )

# print(ElbowBlade('piercing wing').get_desc())

class SmashFist(Weapons):
    str_req = 15
    skill_req = 3
    dam = 2 * Player.strength + Player.skill
    stam_drain = 15
    desc = (
    """
    Another distinct weapon of the New Workshop under the Great One Assembly.
    The Infernal Sledges are a sluggish pair of solid metal bricks attached to
    each hand. Upon transformation, the gauntlets become self-contained
    furnaces that release devastating strikes of hellfire.

    One may easily give in to the temptation of beating one's enemies into
    a burning totem, which leaves one unfortunately vulnerable to a
    self-damaging combustion.
    """
    )

# print(SmashFist('infernal sledges').get_desc())

# class Gear():
#     #def __init__(self):
#         self.helmet = 'dsdsds'
#         self.body = 'asdwewe'
#         self.arms = 'ddsdsd'
#         self.legs = 'wwww'
#         self.accessory = 'eedsd'
#         self.weapon = 'aaweqwe'
#
#     def gear_dict(self):
#         print(self.helmet)
#
#
# class Person():
#     def __init__(self, name, alignment, health, atk):
#         self.name = name
#         self.alignment = alignment
#         self.health = health
#         self.atk = atk
#         self.gear = Gear()
#         #self.aggro = Aggro()
#
# class Player(Person):
#     def __init__(self, name, alignment, health, atk):
#         super().__init__(name, alignment, health, atk)
#
#     def desc_pl(self):
#         return f"{self.name}, {self.gear}"
#
# # class PlayerActions(Player):
# #     def __init__(self, name, alignment, health, atk):
# #         super().__init__(name, alignment, health, atk)
# #         self.gear = Gear()
# #         self.player_data = Player()
#
#     def check_equip(self):
#         equipped = {}
#         equipped['helmet'] = self.helmet
#
# player = Player('www', '1111', 'dddd', '3232')
#
# print(player.check_equip())
# #print(player.desc_pl())
