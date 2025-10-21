from lib.main import *


def test_character_creation():
    player1 = Character("Bilbo")
    assert player1.name == "Bilbo"
    assert player1.health == 100
    assert player1.inv == []


# """
# The player is created with and health is returned
# """

def test_character_health():
    player1 = Character("Bilbo")
    assert player1.get_health() == 100

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
# def test_use_item():
#     player1 = Character("Stevie")
#     potion = Item("Health Potion")
#     player1.add_item(potion)
#     player1.use_item(potion)

#     assert player1.items_list == f"{name} inventory is {inv}"
#     assert player1.health == 100
    

# """
# Given a Player is attacked and health should be reduced

# """
# def test_get_health_when_50_damage():
#     player1 = Character("Stevie")
#     player2 = Character("evil steve")
#     sword = Item("Big Sword", -50)
#     player2.add_item(sword)
#     player2.use_item(sword, player1)

#     assert player1.get_health == f"{name} health is {health}" 
#     # thses might be backwards

# """
# Given a Player is attacked and health is 0 player should be dead

# """
# def test_get_health_when_100_damage():
#     player1 = Character("Stevie")
#     player2 = Character("evil steve")
#     sword = Item("Big Sword", -100)
#     player2.add_item(sword)
#     player2.use_item(sword, player1)

#     assert player1.get_health == f"{name} is dead! {name} health is {health}"