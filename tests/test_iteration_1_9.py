import pytest
from evercraft.models.character import Character

"""
#### Feature: A Character Can Level

> As a character I want my experience points to increase my level and combat capabilities so that I can bring vengeance to my foes

- Level defaults to 1
- After 1000 experience points, the character gains a level
    - 0 xp -> 1st Level
    - 1000 xp -> 2nd Level
    - 2000 xp -> 3rd Level
    - etc.

Every time a level changes, add 5 + constitution modifier to hitpoints 
    
* 1 is added to attack roll for every EVEN level achieved
"""

def test_1st_level():
    c = Character()
    assert c.level == 1

def test_2nd_level():
    c = Character()
    c.xp = 990
    c.add_xp()
    assert c.level == 2

def test_10th_level():
    c = Character()
    c.xp = 9500
    c.add_xp()
    assert c.level == 10

def test_level_change_update_hit_points():
    c = Character()
    c.xp = 1090
    c.constitution = '15'
    c.add_xp()
    assert c.hit_points == 12
    
def test_level_change_update_hit_points_neg():
    c = Character()
    c.xp = 1090
    c.constitution = '5'
    c.add_xp()
    assert c.hit_points == 7

def test_add_one_to_even_level():
    c = Character()
    opponent = Character()
    c.level = 2
    c.attack_attempt(opponent, 13)
    assert c.hit(opponent)
    

