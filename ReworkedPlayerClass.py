import sys

class Base_Character():
    def __init__(self, name, weapon, hp=100, defense=50, damage=5, dodge=2, crit_chance=10, crit_hit=120):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.defense = defense
        self.damage = damage
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.crit_hit = crit_hit

    def modify_class_stats(self):
        if self.name == "Knight":
            self.hp = 110
            self.defense = 70
            self.damage = 10
        elif self.name == "Guardian":
            self.hp = 220
            self.defense = 100
            self.damage = 3
        elif self.name == "Hunter":
            self.hp = 60
            self.defense = 20
            self.dodge = 0.15
            self.crit_chance = 0.15
            self.crit_hit = 150
            
def select_class(user_selection):
    user_class = PlayerClass_Dict.get(user_selection)
    playerclass = None
    if user_class == "Knight":
        playerclass = Base_Character(user_class, "Sword")
        playerclass.modify_class_stats()
    elif user_class == "Guardian":
        playerclass = Base_Character(user_class, "Shield")
        playerclass.modify_class_stats()
    elif user_class == "Hunter":
        playerclass = Base_Character(user_class, "Bow")
        playerclass.modify_class_stats()
    return playerclass

sys.stdout.write("Insert Name: ")
name = sys.stdin.readline()
sys.stdout.write("Sup " +name+ "Pick your class: ")
PlayerClass_Dict = {"1":"Knight", "2":"Guardian", "3":"Hunter"}
sys.stdout.write(str(PlayerClass_Dict)+": ")
pick_class = sys.stdin.readline().rstrip()

selected_class = select_class(pick_class)
sys.stdout.write("\nYou're now a: "+(selected_class.name)+
                 "\n==========Here are your new stats==========\n" 
                 "HP: "+str(selected_class.hp)+ 
                 "\nDefense: "+str(selected_class.defense)+ 
                 "\nDamage: "+str(selected_class.damage)+
                 "\nDodge: "+str(int(selected_class.dodge*100))+"%"
                 "\nCrit Chance: "+str(int(selected_class.crit_chance*100))+"%"
                 "\nCrit Damage: "+str(selected_class.crit_hit)+"%"
                 "\n===========================================")
# PWR = PWR + damage * 0.5
# AGI = AGI + Dodge / 0.5
# VIT = VIT + HP * 1.5
# DEX = Hit chance
# LUK = LUK + Critical chance / 2.5

#Player = Base_Stats ("Roland", "Sword", 5, 5, 5, 5, 5)
#sys.stdout.write("Your Damage is: " +str(Player.PWR*Player.damage*0.25)+"\n") #Damage test
# sys.stdout.write("Your Dodge rate is: "+str(Player.AGI/Player.dodge)+"\n") #Dodge test
# sys.stdout.write("Your HP is: "+str(Player.hp+Player.VIT*1.5)+"\n") #HP test
# sys.stdout.write("Your Defense is: "+str(Player.defense+Player.VIT*0.5)+"\n")#Defense test
# sys.stdout.write("Your Hit chance is: "+str(Player.DEX)+"\n") #Hit test
# sys.stdout.write("Your Crit Chance is: "+str(Player.LUK*Player.crit_chance/25)+"\n")#Crit test
# sys.stdout.write("Crit damage is: " +str(Player.crit_hit)+"%") #Crit Damage test
