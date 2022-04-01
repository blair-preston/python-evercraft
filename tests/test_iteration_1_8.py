import pytest
from evercraft.models.character import Character


"""
#### Feature: A Character can gain experience when attacking

> As a character I want to accumulate experience points (xp) when I attack my enemies so that I can earn bragging rights at the tavern

- When a successful attack occurs, the character gains 10 experience points
"""
# does a character gain xp points with each hit/ critical hit
def test_xp_hit_or_critical_hit():
    dice_roller = Character()
    opponent = Character()
    dice_roller.attack_attempt(opponent, 18)
    assert dice_roller.xp == 10

# character does not get xp points with a miss
def test_xp_miss():
    dice_roller = Character()
    opponent = Character()
    dice_roller.attack_attempt(opponent, 5)
    assert dice_roller.xp == 0
    