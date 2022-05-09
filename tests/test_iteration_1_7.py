import pytest
from evercraft.models.character import Character

#### Feature: Character Ability Modifiers Modify Attributes
'''
> As a character I want to apply my ability modifiers improve my capabilities in combat so that I can vanquish my enemy with extreme prejudice

- add Strength modifier to:
    - attack roll (dice_roller dice number) and damage dealt (opponent hit points)
    - double Strength modifier on critical hits
    -  minimum damage is always 1 (even on a critical hit)
- add Dexterity modifier to armor class
- add Constitution modifier to hit points (always at least 1 hit point)
'''

# Added strength modified to attack roll and damage dealt
def test_add_strength_modifier():
    dice_roller = Character()
    dice_roller.strength = '16'
    opponent = Character()
    assert dice_roller.attack_attempt(opponent, 3) == dice_roller.miss(opponent)

# Added strength modifier to damage dealt
def test_strength_applied_to_damage_hit():
    dice_roller = Character()
    dice_roller.strength = '12'
    opponent = Character()
    assert dice_roller.hit(opponent) == 3

# Added strength modifier to critical hit
def test_strength_applied_to_damage_critical_hit():
    dice_roller = Character()
    dice_roller.strength = '13'
    opponent = Character()
    assert dice_roller.critical_hit(opponent) == 1

# Strength modifier doesn't affect miss
def test_strength_miss():
    dice_roller = Character()
    dice_roller.strength = '19'
    opponent = Character()
    assert dice_roller.miss(opponent) == 5

# Min damage is always 1 if a negative modifier with a regular hit
def test_negative_mod_hit():
    dice_roller = Character()
    dice_roller.strength = '7'
    opponent = Character()
    assert dice_roller.hit(opponent) == 4

# Min damage is always 1 if a negative modifier with a critical hit
def test_negative_critical_hit():
    dice_roller = Character()
    dice_roller.strength = '1'
    opponent = Character()
    assert dice_roller.critical_hit(opponent) == 4

# Added dexterity modifier to armor class
def test_armor_class_update_with_dex():
    c = Character()
    c.set_dexterity('14')
    assert c.armor_class == 12

# Added constitution modifier to hit points
def test_add_const_to_hit_points():
    c = Character()
    c.set_constitution('12')
    assert c.hit_points == 6

# Constitution always adds 1 to hit points even with negative modifier
def test_add_const_at_least_one():
    c = Character()
    c.set_constitution('3')
    assert c.hit_points == 6