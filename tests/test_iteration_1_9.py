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

# can a character have a level
def test_1st_level():
    c = Character()
    assert c.level == 1

# does level change with xp points
def test_2nd_level():
    c = Character()
    c.xp = 990
    c.add_xp()
    assert c.level == 2

# checking that higher levels work
def test_10th_level():
    c = Character()
    c.xp = 9500
    c.add_xp()
    assert c.level == 10

# does changing levels update hit points
def test_level_change_update_hit_points():
    c = Character()
    c.xp = 1090
    c.constitution = '15'
    c.add_xp()
    assert c.hit_points == 12
    
# update hit points example with neg modifier ( + 5 -3 == +2)
def test_level_change_update_hit_points_neg():
    c = Character()
    c.xp = 1090
    c.constitution = '5'
    c.add_xp()
    assert c.hit_points == 7

# even levels +1 to roll
def test_add_one_to_even_level():
    c = Character()
    opponent = Character()
    c.level = 2
    assert c.attack_attempt(opponent, 13) == 4

 # a character with level one does not get +1 added to the roll   
def test_miss():
    c = Character()
    opponent = Character()
    c.level = 1
    assert c.attack_attempt(opponent, 9) == 5

# the same situation as above but being a level two adds 
# one to the number roll and then hits
def test_hit_with_level_points():
    c = Character()
    opponent = Character()
    c.level = 2
    assert c.attack_attempt(opponent, 9) == 4
