import sys
class Base_Character:
    def __init__(self, name, weapon, hp=100, defense=100, damage=5,
                 dodge=0, crit_chance=0, crit_hit=120, pwr=5, agi=5, vit=5, dex=5, luk=5):
        self.name = name
        self.weapon = weapon
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

    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name 
    def get_weapon(self):
        return self.weapon
    def set_weapon(self, weapon):
        self.weapon = weapon
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
    def get_pwr(self):
        return self.pwr
    def set_pwr(self, pwr):
        self.pwr = pwr
    def get_agi(self):
        return self.agi
    def set_agi(self, agi):
        self.agi = agi
    def get_vit(self):
        return self.vit
    def set_vit(self, vit):
        self.vit = vit
    def set_dex(self):
        return self.dex
    def get_dex(self, dex):
        self.dex = dex
    def set_luk(self):
        return self.luk
    def get_luk(self, luk):
        self.luk = luk
        
    def get_crit_percentage(self):
        return str(int(self.get_crit_chance()*100))+"%"
        

    def set_class_stats(self):
        if self.name == "Knight":
            self.hp = 110
            self.defense = 70
            self.damage = 10
            self.dodge = 0
            self.crit_chance = 0
            self.crit_hit = 0
        elif self.name == "Guardian":
            self.hp = 220
            self.defense = 70
            self.damage = 10
            self.dodge = 0
            self.crit_chance = 0
            self.crit_hit = 0
        elif self.name == "Hunter":
            self.hp = 60
            self.defense = 20
            self.dodge = 0.15
            self.crit_chance = 0.15
            self.crit_hit = 150
            
        def increase_attribute(self, selected_attribute):
            self.pwr = self.selected_attribute+1
            
            pass
            
        #elif self.name == "New Class":
        #Create function to Attack - return damage after modifying
        #Create function to check HP - check if self.hp = 0
        #Create function to modify HP - result from attack function & modifying self.hp 
        #Create Monster Class 

def select_class(user_selection): #parameter user selection is a number of string type
    user_class = PlayerClass_Dict.get(user_selection) #gets class name from PlayerClass_Dict base on user input
    playerclass = None #This variable store Base_Character object
    if user_class == "Knight":
        playerclass = Base_Character(user_class, "Sword")
        playerclass.set_class_stats()
    elif user_class == "Guardian":
        playerclass = Base_Character(user_class, "Shield")
        playerclass.set_class_stats()
    elif user_class == "Hunter":
        playerclass = Base_Character(user_class, "Bow")
        playerclass.set_class_stats()
        
    return playerclass

sys.stdout.write("Insert Name: ") #Prompt for Name
name = sys.stdin.readline() #Input name
sys.stdout.write("Sup " +name+ "Pick your class: ") #Prompt for class selection
PlayerClass_Dict = {"1":"Knight", "2":"Guardian", "3":"Hunter"} #Dictionary of class
sys.stdout.write(str(PlayerClass_Dict)+": ") #Print weapon_dict
pick_class = sys.stdin.readline().rstrip() #.rstrip because of invisible new line / #Gets user number input
selected_class = select_class(pick_class) #Passes user input to select_class
sys.stdout.write("\nYou're now a: "+(selected_class.get_name())+
                 "\n==========Here are your new stats==========\n" 
                 "HP: "+str(selected_class.get_hp())+ 
                 "\nDefense: "+str(selected_class.get_defense())+ 
                 "\nDamage: "+str(selected_class.get_damage())+
                 "\nDodge: "+str(int(selected_class.get_dodge()*100))+"%"
                 "\nCrit Chance: "+selected_class.get_crit_percentage()+
                 "\nCrit Damage: "+str(selected_class.get_crit_hit())+"%"
                 "\n===========================================")