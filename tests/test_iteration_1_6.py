import pytest
from evercraft.models.character import Character

#### Feature: Character Has Abilities Scores

# > As a character I want to have several abilities so that I am not identical to other characters except in name

# - Abilities are Strength, Dexterity, Constitution, Wisdom, Intelligence, Charisma
# - Ability scores range from 1 to 20 and default to 10
# - Abilities have modifiers according to the following table

# |   Score   | Modifier |   Score   | Modifier |   Score   | Modifier |   Score   | Modifier |
# |:---------:|:--------:|:---------:|:--------:|:---------:|:--------:|:---------:|:--------:|
# |   __1__   |    -5    |   __6__   |    -2    |  __11__   |     0    |  __16__   |    +3    |
# |   __2__   |    -4    |   __7__   |    -2    |  __12__   |    +1    |  __17__   |    +3    |
# |   __3__   |    -4    |   __8__   |    -1    |  __13__   |    +1    |  __18__   |    +4    |
# |   __4__   |    -3    |   __9__   |    -1    |  __14__   |    +2    |  __19__   |    +4    |
# |   __5__   |    -3    |  __10__   |     0    |  __15__   |    +2    |  __20__   |    +5    |

# does each instance have all abilities?
def test_does_character_have_strength():
    c = Character()
    assert c.strength == '10' 

# does a character have charisma
def test_does_character_have_charisma():
    c = Character()
    assert c.charisma == '10' 

# does each ability score value have a modifier pair?
def test_do_abilites_have_modifiers():
    c = Character()
    assert c.ABILITIES_DICT["14"] == 2

# does our abilities have modifiers avaliable from the dictionary
def test_do_abilites_have_modifiers_test2():
    c = Character()
    assert c.ABILITIES_DICT["5"] == -3
