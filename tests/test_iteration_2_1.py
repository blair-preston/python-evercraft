import pytest
from evercraft.models.character import Character, Fighter, Rogue

'''

> As a player I want to play a ROGUE so that I can defeat my enemies with finesse

- ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
- adds Dexterity modifier to attacks instead of Strength
- cannot have Good alignment

> As a player I want to play a MONK so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting

- has 6 hit point per level instead of 5
- does 3 points of damage instead of 1 when successfully attacking
- adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
- attack roll is increased by 1 every 2nd and 3rd level

> As a player I want to play a PALADIN so that I can smite evil, write wrongs, and be a self-righteous jerk

- has 8 hit points per level instead of 5
- +2 to attack and damage when attacking Evil characters
- does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
- attacks roll is increased by 1 for every level instead of every other level
- can only have Good alignment
'''
# FIGHTER

# can we make an instance of fighter
def test_make_fighter():
    f = Fighter()
    assert isinstance(f, Fighter)

# can we increase roll EVERY level for a fighter...would be a miss for a character, but fighter hits
def test_attack_roll_increase_one_every_level():
    dice_roller = Fighter()
    dice_roller.level = 5
    opponent = Character()
    assert dice_roller.attack_attempt(opponent, 7) == 4

# fighter can still miss, 5 gets added to dice but still less than 10
def test_attack_roll_increase_one_every_level_miss():
    dice_roller = Fighter()
    dice_roller.level = 5
    opponent = Character()
    assert dice_roller.attack_attempt(opponent, 3) == 5

# fighter gets 10 hp points per level
def test_fighter_gets_10hp():
    f = Fighter()
    f.xp = 990
    f.add_xp()
    assert f.hit_points == 15


# ROGUE

# can we make an instance of a rogue
def test_make_rogue():
    r = Rogue()
    assert isinstance(r, Rogue)

# rogue triples damage for critical hits
def test_rogue_triples_damage():
    dice_roller = Rogue()
    opponent = Character()
    assert dice_roller.attack_attempt(opponent, 20) == -1

# while fighting a rogue, dex mod is taken off of your AC if positive
# then switched back to normal when done fighting
def test_rogue_ignore_dex_pos_mod():
    dice_roller = Rogue()
    opponent = Character()
    opponent.set_dexterity('14')
    dice_roller.hit(opponent)
    assert opponent.armor_class == 12

# if dex mod is negatively impacting opponent AC, it still gets applied
def test_rogue_ignore_dex_neg_mod():
    dice_roller = Rogue()
    opponent = Character()
    opponent.set_dexterity('4')
    dice_roller.hit(opponent)
    assert opponent.armor_class == 7






