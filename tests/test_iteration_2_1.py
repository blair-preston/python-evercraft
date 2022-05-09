import pytest
from evercraft.models.character import Character, Fighter, Rogue, Monk, Paladin 

"""
### Iteration 2 - Classes

Classes that a character can have.

#### Feature: Characters Have Classes

> As a player I want a character to have a class that customizes its capabilities so that I can play more interesting characters

##### Ideas

- changes in hit points
- changes in attack and damage
- increased critical range or damage
- bonuses/penalties versus other classes
- special abilities
- alignment limitations

##### Samples

> As a player I want to play a Fighter so that I can kick ass and take names

- attacks roll is increased by 1 for every level instead of every other level
- has 10 hit points per level instead of 5

> As a player I want to play a Rogue so that I can defeat my enemies with finesse

- does triple damage on critical hits
- ignores an opponents Dexterity modifier (if positive) to Armor Class when attacking
- adds Dexterity modifier to attacks instead of Strength
- cannot have Good alignment

> As a player I want to play a Monk so that I can enjoy being an Asian martial-arts archetype in a Medieval European setting

- has 6 hit point per level instead of 5
- does 3 points of damage instead of 1 when successfully attacking
- adds Wisdom modifier (if positive) to Armor Class in addition to Dexterity
- attack roll is increased by 1 every 2nd and 3rd level

> As a player I want to play a Paladin so that I can smite evil, write wrongs, and be a self-righteous jerk

- has 8 hit points per level instead of 5
- +2 to attack and damage when attacking Evil characters
- does triple damage when critting on an Evil character (i.e. add the +2 bonus for a regular attack, and then triple that)
- attacks roll is increased by 1 for every level instead of every other level
- can only have Good alignment
"""

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

# rogue adds dex not strength to attack roll
def test_add_dex_to_attack():
    dice_roller = Rogue()
    opponent = Character()
    dice_roller.set_dexterity('16')
    assert dice_roller.attack_attempt(opponent, 7) == 4

# can code handle error for rogue not allowed to be Good
def test_rogue_cant_be_good():
    r = Rogue()
    assert r.set_alignment("Good") == "Rogues cannot be of Good alignment"


# MONK

# can we make an instance of monk
def test_make_monk():
    m = Monk()
    assert isinstance(m, Monk)

# monk gets 6 hp points per level
def test_monk_gets_6hp():
    m = Monk()
    m.xp = 990
    m.add_xp()
    assert m.hit_points == 11

# monk damages 3 points when attacking for hit and critical hit
def test_monk_has_3_points_damage():
    m = Monk()
    opponent = Character()
    assert m.attack_attempt(opponent, 14) == 2
    
# monk damages 3 points when attacking for hit and critical hit
def test_monk_has_3_points_damage_critical():
    m = Monk()
    opponent = Character()
    assert m.attack_attempt(opponent, 20) == 2

# does wisdom mod get added to AC
def test_add_wisdom():
    m = Monk()
    m.set_wisdom('12')
    assert m.armor_class == 11

# does wisdom mod not get added if negative
def test_dont_add_wisdom_if_mod_neg():
    m = Monk()
    m.set_wisdom('6')
    assert m.armor_class == 10

# does attack roll get the right number added on 2nd and 3rd levels
def test_attack_roll_2nd_3rd_level():
    dice_roller = Monk()
    opponent = Character()
    dice_roller.level = 5
    assert dice_roller.attack_attempt(opponent, 7) == 2

# PALADIN

# can we make an instance of paladin
def test_make_paladin():
    p = Paladin()
    assert isinstance(p, Paladin)

# paladin gets 6 hp points per level
def test_paladin_gets_8hp():
    p = Paladin()
    p.xp = 990
    p.add_xp()
    assert p.hit_points == 13

# paladin gets 2 added to roll
def test_paladin_gets_2_added_to_each_roll():
    p = Paladin()
    opponent = Character()
    opponent.set_alignment('Evil')
    assert p.attack_attempt(opponent, 8) == 2

# paladin's evil opponent gets +2 damage then the normal 
def test_paladin_gets_2_added_to_damage_each_roll():
    p = Paladin()
    opponent = Character()
    opponent.set_alignment('Evil')
    assert p.attack_attempt(opponent, 12) == 2

# paladin triples damage for critical attack of evil character
def test_paladin_triples_damage_critical():
    p = Paladin()
    opponent = Character()
    opponent.set_alignment('Evil')
    assert p.critical_hit(opponent) == -7

# can we increase roll EVERY level for a paladin...would be a miss for a character, but paladin hits
def test_attack_roll_increase_one_every_level_paladin():
    dice_roller = Paladin()
    dice_roller.level = 5
    opponent = Character()
    opponent.set_alignment('Evil')
    assert dice_roller.attack_attempt(opponent, 1) == 2

# paladin can only be of Good alignment
def test_paladin_can_be_good():
    p = Paladin()
    assert p.set_alignment("Neutral") == "Paladin is Good!"