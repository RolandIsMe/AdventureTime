import sys

#Hello
class Base_Character:
    def __init__(self, name, weapon, hp=100, defense=100, damage=5, parry=0, block=0, dodge=0, crit_chance=0, crit_hit=120):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.defense = defense
        self.damage = damage
        self.parry = parry
        self.block = block
        self.dodge = dodge
        self.crit_chance = crit_chance
        self.crit_hit = crit_hit
    def modify_class_stats(self):
        if self.name == "Knight":
            self.hp = 110
            self.defense = 70
            self.damage = 10
            self.parry = 0.15
        elif self.name == "Guardian":
            self.hp = 220
            self.defense = 100
            self.damage = 3
            self.block = 0.15
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
        
sys.stdout.write("Insert Name: ") #Prompt for Name
name = sys.stdin.readline() #Input name
sys.stdout.write("Sup " +name+ "Pick your class: ") #Prompt for class selection
PlayerClass_Dict = {"1":"Knight", "2":"Guardian", "3":"Hunter"} #Dictionary of class
sys.stdout.write(str(PlayerClass_Dict)+": ") #Print weapon_dict
pick_class = sys.stdin.readline().rstrip() #.rstrip because of invisible new line

selected_class = select_class(pick_class)
sys.stdout.write("\nYou're now a: "+(selected_class.name)+
                 "\n==========Here are your new stats==========\n" 
                 "HP: "+str(selected_class.hp)+ 
                 "\nDefense: "+str(selected_class.defense)+ 
                 "\nDamage: "+str(selected_class.damage)+
                 "\nParry: "+str(int(selected_class.parry*100))+"%"
                 "\nBlock: "+str(int(selected_class.block*100))+"%"
                 "\nDodge: "+str(int(selected_class.dodge*100))+"%"
                 "\nCrit Chance: "+str(int(selected_class.crit_chance*100))+"%"
                 "\nCrit Damage: "+str(selected_class.crit_hit)+"%"
                 "\n===========================================")