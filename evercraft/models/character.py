import math 

# this is where your character code will go

class Character():
    character = {
        'name': "",
    }
    
    # alignment options: 
    ALIGN_EVIL = "Evil"
    ALIGN_GOOD = "Good"
    ALIGN_NEUTRAL = "Neutral"

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

    def __init__(self):
        self.armor_class = 10
        self.hit_points = 5
        self.xp = 0
        self.level = 1
        self.alive = 0

        # abilities
        self.strength = '10'
        self.dexterity = '10'
        self.constitution = '10'
        self.wisdom = '10'
        self.intelligence = '10'
        self.charisma = '10'
        
    
    def set_name(self, character=None):
        if character == None:
            self.name = 'User'
        else:
            self.name = character["name"]

    def get_name(self):
        return self.name

    def set_alignment(self, alignment):
        self.alignment = alignment

    def get_alignment(self):
        return self.alignment
    
    def attack_attempt(self, opponent, number_roll):
        if self.level > 1:
            if self.level % 2 == 0:
                number_roll = number_roll + (self.level / 2)
            elif self.level % 2 != 0:
                number_roll = number_roll + math.floor(self.level / 2)
        attack_roll = number_roll + self.ABILITIES_DICT[self.strength]
        if attack_roll == 20:
            return self.critical_hit(opponent)
        elif attack_roll >= opponent.armor_class:
            return self.hit(opponent)
        elif attack_roll < opponent.armor_class:
            return self.miss(opponent)
    
    def critical_hit(self, opponent):
        self.add_xp()
        subtract_me = (2 + (2 * self.ABILITIES_DICT[self.strength]))
        if subtract_me < 1:
            subtract_me = 1
        opponent.hit_points = opponent.hit_points - subtract_me
        if self.hit_points <= 0:
            self.alive = 0
        return opponent.hit_points
            

    def hit(self, opponent):
        self.add_xp()
        subtract_me = (1 + self.ABILITIES_DICT[self.strength])
        if subtract_me < 1:
            subtract_me = 1
        opponent.hit_points = opponent.hit_points - subtract_me
        if self.hit_points <= 0:
            self.alive = 0
        return opponent.hit_points

    def miss(self, opponent):
        return opponent.hit_points

    def set_dexterity(self, dexVal):
      self.dexterity = dexVal
      self.armor_class = self.armor_class + self.ABILITIES_DICT[self.dexterity]

    def set_constitution(self, consVal):
        self.constitution = consVal
        add_me = self.ABILITIES_DICT[self.constitution]
        if add_me < 1:
            add_me = 1
        self.hit_points = self.hit_points + add_me

    def add_xp(self):
        self.xp = self.xp + 10
        if self.xp >= 1000:
            check = math.floor(self.xp / 1000) + 1
            if (check != self.level):
                self.level = check
                self.hit_points = self.hit_points + 5 + self.ABILITIES_DICT[self.constitution]
        
        