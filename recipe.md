# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem
As a game player
I want to create a `character` with a cool `name`
So that other players recognise my character

As a game player
I want to see my characters `health`
So that I know when I might need to drink a health potion

As a game player
I want my character to be able to `pick up` `items (potions/weapons)` that they find in the game
So that they can use them when they need

As a game player
I want to be able to `use my health potion` item
So that my character's health goes back to 100

As a game player
I want to `attack` another character
So that they lose the health points associated with an attack by that weapon

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Character:
    # User-facing properties:
    #   name: string

    def __init__(self, name, health, inv):
        # Parameters:
        #   name: string
        #   health: int
        #   items: list

        # Side effects:
        #   Sets the name property of the self object
        #   sets health for obj
        #  sets empty list for items
        pass # No code here yet

    def get_health(self):
        # Parameters:
        #   task: int reperesetning characters health
        # Returns:
        #   characters health in 
        # Side-effects
        pass # No code here yet

    def pick_up_items(self):
        # Paramters:
        #    Appends "item" to item list, representing an item
        #    Should inherit from a  class "item".
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def use_item(self, item, target):
        #finds item in inventory and uses it and is removed from inventory.
        #look at items_list
        # have an effect * always a postive effect to health + *
        # needs to inheret effect from items class
        pass

    # def use_attack(self, item, target):
    #     #finds item in inventory and uses it and is removed from inventory.
    #     #look at items_list
    #     # have a target. ie. self or other character
    #     # have an effect * always an effect to health + or - *
    #     # needs to inheret effect from items class
    #     pass

    # select item to use and who to use it on


class Items:
    # User-facing properties:
    #   name: string

    def __init__(self, item_name, item_effect)
     self.item = name
     self.effect = effect

     health = item(healthpotion, -50)
    pass

# use

 
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
The player is created with a cool name, health and a empty inventory
"""

def test_character_creation():
    player1 = Character("Bilbo")
    assert player1.name == "Bilbo"
    assert player1.health == 100
    assert player1.inv == []


"""
The player is created with and health is returned
"""

def test_character_health():
    player1 = Character("Bilbo")
    assert player1.gethealth() == 100

"""
The player collects an item and it is added to the inventory
"""
def test_pick_up_item():
    player1 = Character("Stevie")
    potion = Item("Health Potion")
    player1.add_item(potion)
    assert player1.items_list == [potion]


"""
The player collects 2 items and they are added to the inventory
"""
def test_pick_up_item():
    player1 = Character("Stevie")
    potion = Item("Health Potion")
    sword = Item("Big sword")
    player1.pick_up_item(potion)
    player.pick_up_item(sword)
    assert len(player1.inv) == 2


"""
The player uses an item and it effects are applied and
is removed to the inventory
"""
def test_use_item():
    player1 = Character("Stevie")
    potion = Item("Health Potion")
    player1.add_item(potion)
    player1.use_item(potion)

    assert player1.items_list == f"{name} inventory is {item_list}"
    

"""
Given a Player is attacked and health should be reduced

"""
def test_get_health_when_50_damage():
    player1 = Character("Stevie")
    player2 = Character("evil steve")
    sword = Item("Big Sword", -50)
    player2.add_item(sword)
    player2.use_item(sword, player1)

    assert player1.get_health == f"{name} health is {health}" 
    # thses might be backwards

"""
Given a Player is attacked and health is 0 player should be dead

"""
def test_get_health_when_100_damage():
    player1 = Character("Stevie")
    player2 = Character("evil steve")
    sword = Item("Big Sword", -100)
    player2.add_item(sword)
    player2.use_item(sword, player1)

    assert player1.get_health == f"{name} is dead! {name} health is {health}"

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
