import pytest
from evercraft.models.character import Character

'''
#### Feature: Character Can Be Damaged

> As an attacker I want to be able to damage my enemies so that they will die and I will live

- If attack is successful, other character takes 1 point of damage when hit
- If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
- when hit points are 0 or fewer, the character is dead
'''

def test_hit():
    dice_roller = Character()
    opponent = Character()
    dice_roller.hit(opponent)
    assert opponent.hit_points == 4

def test_critical_hit():
    dice_roller = Character()
    opponent = Character()
    dice_roller.critical_hit(opponent)
    assert opponent.hit_points == 3

def test_miss():
    dice_roller = Character()
    opponent = Character()
    dice_roller.miss(opponent)
    assert opponent.hit_points == 5

def test_dead():
    c = Character()
    c.hit_points == 0
    assert c.life_status == 'dead'
    