# this is where your character code will go

class Character():
    character = {
        'name': "",
    }
    
    # alignment options: 
    ALIGN_EVIL = "Evil"
    ALIGN_GOOD = "Good"
    ALIGN_NEUTRAL = "Neutral"

    def __init__(self):
        self.armor_class = 10
        self.hit_points = 5
        self.life_status = 'alive'
    
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
        if number_roll == 20:
            return critical_hit()
        elif number_roll >= opponent.armor_class:
            return hit()
        elif number_roll < opponent.armor_class:
            return miss()
    
    def critical_hit(self, opponent):
        opponent.hit_points = opponent.hit_points - 2

    def hit(self, opponent):
        opponent.hit_points = opponent.hit_points - 1

    def miss(self, opponent):
        opponent.hit_points

    def death(self):
        if self.hit_points == 0:
            self.life_status = 'dead'