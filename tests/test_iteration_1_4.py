import pytest
from evercraft.models.character import Character




#### Feature: Character Can Attack
'''
> As a combatant I want to be able to attack other combatants so that I can survive to fight another day

- roll a 20 sided die (don't code the die)
- roll must meet or beat opponents armor class to hit
- a natural roll of 20 always hits
'''
# player can hit with a dice roll higher than opponent armor class
def test_can_attack_hit():
    dice_roller = Character()
    opponent = Character()
    assert  dice_roller.attack_attempt(opponent, 15) == 4

# player will miss with a dice roll lower than opponent armor class    
def test_can_attack_miss():
    dice_roller = Character()
    opponent = Character()
    assert dice_roller.attack_attempt(opponent, 5) == dice_roller.miss(opponent)

# player will always hit with roll of 20
def test_can_attack_hit_20():
    dice_roller = Character()
    opponent = Character()
    assert dice_roller.attack_attempt(opponent, 20) == 3