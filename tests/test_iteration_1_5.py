import pytest
from evercraft.models.character import Character

'''
#### Feature: Character Can Be Damaged

> As an attacker I want to be able to damage my enemies so that they will die and I will live

- If attack is successful, other character takes 1 point of damage when hit
- If a roll is a natural 20 then a critical hit is dealt and the damage is doubled
- when hit points are 0 or fewer, the character is dead
'''

# what does a hit do?
# opponent loses 1 hit point
def test_hit():
    dice_roller = Character()
    opponent = Character()
    dice_roller.hit(opponent)
    assert opponent.hit_points == 4

# what does a critical hit do?
# opponent loses 2 hit point
def test_critical_hit():
    dice_roller = Character()
    opponent = Character()
    dice_roller.critical_hit(opponent)
    assert opponent.hit_points == 3

# what does a miss do?
# opponent hit points do not change
def test_miss():
    dice_roller = Character()
    opponent = Character()
    dice_roller.miss(opponent)
    assert opponent.hit_points == 5

# what happens if character hit points is 0?
# opponent is dead (self.alive == 0)
# self.alive == 1 is alive
def test_dead():
    dice_roller = Character()
    opponent = Character()
    opponent.hit_points = 2
    dice_roller.critical_hit(opponent)
    assert opponent.alive == 0
    