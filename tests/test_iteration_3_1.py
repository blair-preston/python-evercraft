import pytest
from evercraft.models.character import Character, Fighter, Rogue, Monk, Paladin, Orc 

'''
### Iteration 3 - Races

Races that a character can be.

#### Feature: Characters Have Races

> As a player I want to play a Human so that I can be boring and unoriginal

- all characters default to Human

> As a player I want a character to have races other than Human that customize its capabilities so that I can play more interesting characters and wont be boring and unoriginal

##### Ideas

- changes in abilities
- increased critical range or damage
- bonuses/penalties versus other races
- special abilities
- alignment limitations

##### Samples

> As a player I want to play an Orc so that I can be crude, drunk, and stupid

- +2 to Strength Modifier, -1 to Intelligence, Wisdom, and Charisma Modifiers
- +2 to Armor Class due to thick hide

> As a player I want to play a Dwarf so that I can drink more than the orc

- +1 to Constitution Modifier, -1 to Charisma Modifier
- doubles Constitution Modifier when adding to hit points per level (if positive)
- +2 bonus to attack/damage when attacking orcs (Dwarves hate Orcs)

> As a player I want to play an Elf so that I can drink wine and snub my nose at the crude dwarf and orc

- +1 to Dexterity Modifier, -1 to Constitution Modifier
- does adds 1 to critical range for critical hits (20 -> 19-20, 19-20 -> 18-20)
- +2 to Armor Class when being attacked by orcs

> As a player I want to play a Halfling so that I can steal from the other drunk characters

- +1 to Dexterity Modifier, -1 to Strength Modifier
- +2 to Armor Class when being attacked by non Halfling (they are small and hard to hit)
- cannot have Evil alignment
'''

# is an instance human on default
def test_default_human():
    c = Character()
    assert c.race == "Human"

def test_orc_exists():
    o = Orc()
    assert isinstance(o, Orc)

