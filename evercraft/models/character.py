from math import ceil, floor  

class Character():

    # alignment options: 
    ALIGN_EVIL = "Evil"
    ALIGN_GOOD = "Good"
    ALIGN_NEUTRAL = "Neutral"

    # Ability modifier dictionary
    ABILITIES_DICT = {
        "1": -5,
        "2": -4,
        "3": -4,
        "4": -3,
        "5": -3,
        "6": -2,
        "7": -2,
        "8": -1,
        "9": -1,
        "10": 0,
        "11": 0,
        "12": 1,
        "13": 1,
        "14": 2,
        "15": 2,
        "16": 3,
        "17": 3,
        "18": 4,
        "19": 4,
        "20": 5,
    }

    #### ID counter for Characters
    class_counter = 0

    def __init__(self, name=None, alignment=None):
        self.armor_class = 10
        self.hit_points = 5
        self.xp = 0
        self.level = 1
        # 1 is truthy, 1 = alive, 0 = dead
        self.alive = 1
        self.race = 'Human'


        #### the following two lines give each instance of Character a unique id
        self.id = Character.class_counter
        Character.class_counter += 1
        

        # abilities
        self.strength = '10'
        self.dexterity = '10'
        self.constitution = '10'
        self.wisdom = '10'
        self.intelligence = '10'
        self.charisma = '10'
        

        # Default of "User" as name and "Neutral" as alignment
        if name is None:
            self.name = 'User'
        else:
            self.name = name
        if alignment is None:
            self.alignment = 'Neutral'
        else:
            self.alignment = alignment
                

     # SETTERS AND GETTERS   
    def get_name(self):
        return self.name

    def set_alignment(self, alignment):
        self.alignment = alignment

    def get_alignment(self):
        return self.alignment

    def set_dexterity(self, dexVal):
      self.dexterity = dexVal
      self.armor_class = self.armor_class + self.ABILITIES_DICT[self.dexterity]

    # if const. is updated, hit points also need to be updated
    def set_constitution(self, consVal):
        self.constitution = consVal
        add_me = self.ABILITIES_DICT[self.constitution]
        if add_me < 1:
            add_me = 1
        self.hit_points = self.hit_points + add_me
    
    ####
    def attack_attempt(self, opponent, number_roll):
        # +1 to dice for every even level reached
        if self.level > 1:
            number_roll = number_roll + floor(self.level / 2)

        # updated number_roll + strength determines the outcome of attack attempt
        attack_roll = number_roll + self.ABILITIES_DICT[self.strength]

        # CRITICAL HIT
        if attack_roll == 20:
            return self.critical_hit(opponent)

        # HIT
        elif attack_roll >= opponent.armor_class:
            return self.hit(opponent)

        # MISS
        elif attack_roll < opponent.armor_class:
            return self.miss(opponent)
    
    def critical_hit(self, opponent):
        self.add_xp()
        subtract_me = (2 + (2 * self.ABILITIES_DICT[self.strength]))
        if subtract_me < 1:
            subtract_me = 1
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0:
            opponent.alive = 0
        return opponent.hit_points
            
    def hit(self, opponent):
        self.add_xp()
        subtract_me = (1 + self.ABILITIES_DICT[self.strength]) 
        if subtract_me < 1: 
            subtract_me = 1 
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0: 
            opponent.alive = 0
        return opponent.hit_points
    
    def miss(self, opponent):
        return opponent.hit_points

    #### any attack --> +10 xp AND checks level increase every time 
    def add_xp(self):
        self.xp = self.xp + 10
        if self.xp >= 1000:
            check = floor(self.xp / 1000) + 1
            if (check != self.level):
                self.level = check
                self.hit_points = self.hit_points + 5 + self.ABILITIES_DICT[self.constitution]
    

    #### CALLED FROM ROGUE CLASS
    def fix_AC(self):
      # from ROGUE class...Rogue opponent doesn't get to apply dex to AC
        self.armor_class = self.armor_class - self.ABILITIES_DICT[self.dexterity]
        return self.armor_class

    def switch_back_AC(self):
        # from ROGUE class...Rogue opponent gets dex back after attack
        self.armor_class = self.armor_class + self.ABILITIES_DICT[self.dexterity]
        return self.armor_class



# THE FOLLOWING CLASSES ARE CHILDREN OF CHARACTER CLASS:

class Fighter(Character):
    # Attack roll is increased by ONE for EVERY level instead of every other level
    # 10 XP added per level instead of 5
    def attack_attempt(self, opponent, number_roll):
        attack_roll = number_roll + self.ABILITIES_DICT[self.strength] + self.level
        if attack_roll == 20:
            return self.critical_hit(opponent)
        elif attack_roll >= opponent.armor_class:
            return self.hit(opponent)
        elif attack_roll < opponent.armor_class:
            return self.miss(opponent)

    def add_xp(self):
        self.xp = self.xp + 10
        if self.xp >= 1000:
            check = floor(self.xp / 1000) + 1
            if (check != self.level):
                self.level = check
                self.hit_points = self.hit_points + 10 + self.ABILITIES_DICT[self.constitution]

class Rogue(Character):
    # Triple damage on critical hits
    # Opponent cannot use POSITIVE dex modifier to increase armor class
    # Cannot have Good alignment
    # Sub strength for dex modifier in attack roll
    def attack_attempt(self, opponent, number_roll):
        if self.level > 1:
            if self.level % 2 == 0:
                number_roll = number_roll + (self.level / 2)
            elif self.level % 2 != 0:
                number_roll = number_roll + floor(self.level / 2)
        attack_roll = number_roll + self.ABILITIES_DICT[self.dexterity]
        if attack_roll == 20:
            return self.critical_hit(opponent)
        elif attack_roll >= opponent.armor_class:
            return self.hit(opponent)
        elif attack_roll < opponent.armor_class:
            return self.miss(opponent)

    def critical_hit(self, opponent):
        if (opponent.ABILITIES_DICT[opponent.dexterity]) > 0:
            opponent.fix_AC()
        self.add_xp()
        subtract_me = ((2*3) + (2 * self.ABILITIES_DICT[self.strength]))
        if subtract_me < 1:
            subtract_me = 1
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0:
            opponent.alive = 0
        if (opponent.ABILITIES_DICT[opponent.dexterity]) > 0:
            opponent.switch_back_AC()
        return opponent.hit_points
            

    def hit(self, opponent):
        ####
        if (opponent.ABILITIES_DICT[opponent.dexterity]) > 0:
            opponent.fix_AC()
        self.add_xp()
        subtract_me = (1 + self.ABILITIES_DICT[self.strength]) 
        if subtract_me < 1: 
            subtract_me = 1 
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0: 
            opponent.alive = 0
        ####
        if (opponent.ABILITIES_DICT[opponent.dexterity]) > 0:
            opponent.switch_back_AC()
        return opponent.hit_points

    def set_alignment(self, alignment):
        if alignment == 'Good':
            return "Rogues cannot be of Good alignment"
        else:
            self.alignment = alignment

class Monk(Character):
    # 6 HP per level instead of 5
    # 3 points of damage on successful attack instead of 1
    # armor class is wisdom modifier AND dex modifier
    # Plus one for attack roll every 2nd and 3rd level

    def attack_attempt(self, opponent, number_roll):
        if self.level > 1:
            add_me = self.level - ceil(self.level / 3)
            attack_roll = number_roll + self.ABILITIES_DICT[self.strength] + add_me
        else:
            attack_roll = number_roll + self.ABILITIES_DICT[self.strength]
        if attack_roll == 20:
            return self.critical_hit(opponent)
        elif attack_roll >= opponent.armor_class:
            return self.hit(opponent)
        elif attack_roll < opponent.armor_class:
            return self.miss(opponent)

    def add_xp(self):
        self.xp = self.xp + 10
        if self.xp >= 1000:
            check = floor(self.xp / 1000) + 1
            if (check != self.level):
                self.level = check
                self.hit_points = self.hit_points + 6 + self.ABILITIES_DICT[self.constitution]
    
    def hit(self, opponent):
        self.add_xp()
        subtract_me = (3 + self.ABILITIES_DICT[self.strength]) 
        if subtract_me < 1: 
            subtract_me = 1 
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0: 
            opponent.alive = 0
        return opponent.hit_points

    def critical_hit(self, opponent):
        self.add_xp()
        subtract_me = (3 + (2 * self.ABILITIES_DICT[self.strength]))
        if subtract_me < 1:
            subtract_me = 1
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0:
            opponent.alive = 0
        return opponent.hit_points

    def set_wisdom(self, wisVal):
        self.wisdom = wisVal
        if self.ABILITIES_DICT[self.wisdom] >= 0:
            self.armor_class = self.armor_class + self.ABILITIES_DICT[self.dexterity] + self.ABILITIES_DICT[self.wisdom]
        else:
            self.armor_class = self.armor_class + self.ABILITIES_DICT[self.dexterity]

class Paladin(Character):
    # 8 HP per level instead of 5
    # For EVIL opponents:
        # +2 damage
        # Triple damange for critical hits
    # Attack roll increased by 1 for every level
    # Good alignment ONLY
    def set_alignment(self, alignment):
        if alignment == 'Good':
            self.alignment = alignment
        else:
            return "Paladin is Good!"

    def attack_attempt(self, opponent, number_roll):
        if self.level > 1:
            if self.level % 2 == 0:
                number_roll = number_roll + (self.level / 2)
            elif self.level % 2 != 0:
                number_roll = number_roll + floor(self.level / 2)
        attack_roll = 2 + number_roll + self.ABILITIES_DICT[self.strength] + self.level
        if attack_roll == 20:
            return self.critical_hit(opponent)
        elif attack_roll >= opponent.armor_class:
            return self.hit(opponent)
        elif attack_roll < opponent.armor_class:
            return self.miss(opponent)

    def critical_hit(self, opponent):
        self.add_xp()
        if opponent.alignment == 'Evil':    
            subtract_me = 3 * (2 + 2 + (2 * self.ABILITIES_DICT[self.strength]))
        else: 
            subtract_me = (2 + (2 * self.ABILITIES_DICT[self.strength]))
        if subtract_me < 1:
            subtract_me = 1
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0:
            opponent.alive = 0
        return opponent.hit_points
            
    def hit(self, opponent):
        self.add_xp()
        if opponent.alignment == 'Evil':    
            subtract_me = (1 + 2 + (self.ABILITIES_DICT[self.strength]))
        else: 
            subtract_me = (1 + (self.ABILITIES_DICT[self.strength]))
        if subtract_me < 1: 
            subtract_me = 1 
        opponent.hit_points = opponent.hit_points - subtract_me
        if opponent.hit_points <= 0: 
            opponent.alive = 0
        return opponent.hit_points

    def add_xp(self):
        self.xp = self.xp + 10
        if self.xp >= 1000:
            check = floor(self.xp / 1000) + 1
            if (check != self.level):
                self.level = check
                self.hit_points = self.hit_points + 8 + self.ABILITIES_DICT[self.constitution]



