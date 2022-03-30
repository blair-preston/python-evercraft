import pytest
from evercraft.models.character import Character


#### Feature: Alignment
'''
> As a character I want to have an alignment so that I have something to guide my actions

- can get and set alignment
- alignments are Good, Evil, and Neutral
'''

# can set alignment
def test_canSetAlignment():
    c = Character()
    c.set_alignment(c.ALIGN_EVIL)
    assert c.get_alignment() == "Evil"