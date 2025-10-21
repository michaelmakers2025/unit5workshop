class Character:
    # User-facing properties:
    #   name: string

    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inv = []
        pass
        # Parameters:
        #   name: string
        #   health: int
        #   items: list

#         # Side effects:
#         #   Sets the name property of the self object
#         #   sets health for obj
#         #  sets empty list for items
#         pass # No code here yet

    def get_health(self):
        return self.health
# No code here yet

    def pick_up_item(self, Item):
        # Paramters:
        #    Appends "item" to item list, representing an item
        #    Should inherit from a  class "item".
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        self.inv.append(Item)
        return dir(self.inv)

#     def use_item(self, item, target):
#         #finds item in inventory and uses it and is removed from inventory.
#         #look at items_list
#         # have an effect * always a postive effect to health + *
#         # needs to inheret effect from items class
#         pass

#     # def use_attack(self, item, target):
#     #     #finds item in inventory and uses it and is removed from inventory.
#     #     #look at items_list
#     #     # have a target. ie. self or other character
#     #     # have an effect * always an effect to health + or - *
#     #     # needs to inheret effect from items class
#     #     pass

#     # select item to use and who to use it on


class Item:
    # User-facing properties:
    #   name: string

    def __init__(self, item, effect):
        self.item = item
        self.effect = effect