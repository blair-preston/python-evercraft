import pytest
from evercraft.models.character import Character

#### Feature: Armor Class & Hit Points

'''
> As a combatant I want to have an armor class and hit points so that I can resist attacks from my enemies

- has an Armor Class that defaults to 10
- has 5 Hit Points by default
'''

# armor class on init of instance
def test_add_armor_class():
    c = Character()
    assert c.armor_class == 10

# hit points on init of instance
def test_add_hit_points():
    c = Character()
    assert c.hit_points == 5
