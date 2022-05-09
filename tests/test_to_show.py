import pytest
from evercraft.models.character import Character

def test_characters_get_different_ids_1():
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

def test_add_one_to_even_level_1():
    c = Character()
    opponent = Character()
    c.level = 2
    assert c.attack_attempt(opponent, 9) == 4

def test_10th_level_1():
    c = Character()
    c.xp = 9500
    c.add_xp()
    assert c.level == 10