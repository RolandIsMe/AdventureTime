import random
import sys

class Monster: #wrong name? I renamed to Monster
    def __init__(self, name, hp=100, defense=100, damage=5,
                 dodge=0, crit_chance=0, crit_hit=120):
        self.name = name
        self.hp = hp
        self.defense = defense
        self.damage = damage
        self.dodge = dodge  # Don't remember what stats you want for monster so I deleted all attributes and left soem stats. Fix this to what you want this to look like.
        self.crit_chance = crit_chance
        self.crit_hit = crit_hit

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name 
    def get_hp(self):
        return self.hp
    def set_hp(self, hp):
        self.hp = hp 
    def get_defense(self):
        return self.defense
    def set_defense(self, defense):
        self.defense = defense 
    def get_damage(self):
        return self.damage   
    def set_damage(self, damage):
        self.damage = damage
    def get_dodge(self):
        return self.dodge
    def set_dodge(self, dodge):
        self.dodge = dodge
    def get_crit_chance(self):
        return self.crit_chance
    def set_crit_chance(self, crit_chance):
        self.crit_chance = crit_chance
    def get_crit_hit(self):
        return self.crit_hit
    def set_crit_hit(self, crit_hit):
        self.crit_hit = crit_hit

    def modify_monster_stats(self): #INCOMPLETE: Finish this function.
        if self.name == "Kraken":
            self.hp = 100
            self.defense = 10
            self.damage = 15

        elif self.name == "Chimera":
            self.hp = 150
            self.defense = 5
            self.damage = 15

        elif self.name == "Dragon":
            self.hp = 300
            self.defense = 20
            self.damage = 20

def select_monster(monster_list): #Function takes a list of monsters of string type as a parameter and returns an instance of specialized Monster class.
    random_monster = random.choice(monster_list) # Selects a random monster name from the list of monsters and store the string var in random_monster.
    monster_instance = Monster(random_monster) 
    monster_instance.modify_monster_stats()
    return monster_instance

# Execution of program.
monster_list = ["Kraken", "Chimera", "Dragon", "Basilisk", "Goblins",
                "Ogres", "Minotaur", "Ghost", "Zombie", "Banshee"]

monster = select_monster(monster_list) #select a random monster from list and returns it

# Output selected monster name and its stats.
print(f"You've encountered a {monster.get_name()}.") # You'll need to need to rewrite this using std.write or something.
print("*" * 15)
print(f"Monster Stats: \nHP: {monster.get_hp()} \nDEF: {monster.get_defense()} \nDMG: {monster.get_damage()} \nCritical Chance: {monster.get_crit_chance()}")
print("*" * 15)
