import pytest
from evercraft.models.character import Character


#### Feature: Create a Character
# > As a character I want to have a name so that I can be distinguished from other characters
# - can get and set Name

# can we create an instance from class character
def test_createACharacter():
    c = Character()
    assert isinstance(c, Character)

# set a name for the instance and get the name 
def test_characterCanSetName():
    c = Character()
    c.name = 'Fred'
    assert c.get_name() == "Fred"

# set a name for 2 characters
def test_characters():
    c = Character()
    c.name = 'Wilma'
    c2 = Character()
    c2.name = 'Betty'
    assert c.get_name() != c2.get_name()

# set multiple names
def test_lotsOfUsers():
    user_names = [
        'BamBam',
        'Dino',
        'Woody',
        'LittleBoPeep',
        'SlinkyDog',
        'Buzz',
        'Mr.PotatoHead',
        'Mrs.PotatoHead'
    ]
    users = []
    for name in user_names:
        c = Character()
        c.name = name
        users.append(c.name)
    assert len(user_names) == len(users)

# does character have a name given on init
def test_character_gets_name_on_init():
    c = Character()
    assert c.name == "User"

# does character have an alignment given on init
def test_character_gets_alignment_on_init():
    c = Character()
    assert c.alignment == "Neutral"

# does character have an unique id on init
def test_character_id():
    c = Character()
    assert c.id != None


# does multiple characters get different id'set
def test_characters_get_different_ids():
    user_names = [
        'BamBam',
        'Dino',
        'Woody',
        'LittleBoPeep',
        'SlinkyDog',
        'Buzz',
        'Mr.PotatoHead',
        'Mrs.PotatoHead'
    ]
    users_ids = []
    for name in user_names:
        c = Character()
        c.name = name
        users_ids.append(c.id)
    assert users_ids[0] != users_ids[1] != users_ids[2]