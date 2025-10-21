from lib.main import *


def test_character_creation():
    player1 = Character("Bilbo")
    assert player1.name == "Bilbo"
    assert player1.health == 100
    assert player1.inv == []


# """
# The player is created with and health is returned
# """

# def test_character_health():
#     player1 = Character("Bilbo")
#     assert player1.get_health() == 100

# """
# The player collects an item and it is added to the inventory
# """
def test_pick_up_item():
    player1 = Character("Stevie")
    potion = Item("Health Potion", 100)
    player1.pick_up_item(potion)
    assert player1.inv == [potion]


# """
# The player collects 2 items and they are added to the inventory
# """
# def test_pick_up_item():
#     player1 = Character("Stevie")
#     potion = Item("Health Potion")
#     sword = Item("Big sword")
#     player1.pick_up_item(potion)
#     player.pick_up_item(sword)
#     assert len(player1.inv) == 2

def test_pick_up_two_items():
    player2 = Character("Legolas")
    potion = Item("Health Potion", 100)
    sword = Item("Big sword", -50)
    player2.pick_up_item(potion)
    player2.pick_up_item(sword)
    assert list(player2.inv) == [potion, sword]



# """
# The player uses an item and it effects are applied and
# is removed to the inventory
# """
def test_use_item():
    player3 = Character("Stevie")
    potion = Item("Health Potion", effect=100)
    player3.pick_up_item(potion)
    player3.use_item(potion)

    assert player3.inv == [potion]
    assert player3.get_health() == "Stevie health is 200"

# """
# Given a Player is attacked and health should be reduced

# """
def test_get_health_when_50_damage():
    player4 = Character("Stevie")
    player5 = Character("evil steve")
    sword = Item("Big Sword", effect=-50)
    player4.pick_up_item(sword)
    player4.use_item(sword, player5)

    assert player5.get_health() == "evil steve health is 50"
    assert player4.get_health() == "Stevie health is 100"
 
#     # thses might be backwards

# """
# Given a Player is attacked and health is 0 player should be dead

# """
def test_get_health_when_100_damage():
    player7 = Character("Stevie")
    player8 = Character("evil steve")
    sword = Item("Big Sword", -100)
    player8.pick_up_item(sword)
    player8.use_item(sword, player7)

    assert player7.get_health() == "Stevie health is 0, and is Dead!"