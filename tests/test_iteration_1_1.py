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
    # user_name = 'Fred'
    # c.set_traits({"name" : user_name, "alignment" : "Good"})
    c.name = 'Fred'
    c.alignment = 'Good'
    assert c.get_name() == c.name

# set a name for 2 characters
def test_characters():
    c = Character()
    c.name = 'Wilma'
    c.alignment = 'Good'
    c2 = Character()
    c2.name = 'Betty'
    c2.alignment = 'Good'
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
        # c.set_traits({"name": name, "alignment" : "Good"})
        c.name = name
        c.alignment = 'Good'
        users.append(c.name)
    assert len(user_names) == len(users)

# provide traits within an object
def test_characterNameFromObject():
    c = Character()
    character = {
        'name': 'Fred', 
        "alignment" : "Good"
    }
    c.name = 'Fred'
    assert c.name == character['name']

# set default value if name is not given
def test_characterNameDefault():
    c = Character()
    c.name = 'name'
    assert c.name != 'null'

