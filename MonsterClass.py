import random
import sys

class Base_Character:
    def __init__(self, name, hp=100, defense=100, damage=5,
                 dodge=0, crit_chance=0, crit_hit=120, pwr=5, agi=5, vit=5, dex=5, luk=5):
        self.name = name

        self.hp = hp
        self.defense = defense
        self.damage = damage
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.crit_hit = crit_hit
        self.pwr = pwr
        self.agi = agi
        self.vit = vit
        self.dex = dex
        self.luk = luk

Monster_Dict = {"Kraken", "Chimera", "Dragon", "Basilisk", "Goblins",
                "Ogres", "Minotaur", "Ghost", "Zombie", "Banshee"} #Dictionary of monsters
#sys.stdout.write(str(Monster_Dict)) #Comment out for now

entry_list = Monster_Dict #Call on dictionary for an item
random_entry = random.choice(list(entry_list)) #using random.choice to get a random return
print(random_entry)#Print out random.choice

def monster_test(self):
    if self.name == "Kraken":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Chimera":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Dragon":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Basilisk":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Goblins":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Ogres":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Minotaur":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Ghost":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Zombie":
        self.hp = 10
        self.defense = 10
        self.damage = 10
    elif self.name == "Banshee":
        self.hp = 10
        self.defense = 10
        self.damage = 10


def select_monster(random_selection):
     monster_class = Monster_Dict(random_selection)
     monsterpick = None
     if monster_class == "Kraken": 
         monsterpick = Base_Character(monster_class)
         monsterpick.monster_test()
     elif monster_class == "Chimera": 
         monsterpick = Base_Character(monster_class)
         monsterpick.monster_test()
     elif monster_class == "Dragon":
         monsterpick = Base_Character(monster_class)
         monsterpick.monster_test()
        
     return monsterpick

#selected_monster = select_monster(random_entry)
#sys.stdout.write("You have encountered a: "+str(selected_monster))