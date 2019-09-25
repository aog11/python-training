#Chapter 5
#Adding from list to Fantasy Game Inventory

import random

stuff = {'rope': 1, 'torch': 4, 'cheese': 25, 'ham': 10,
         'potions': 19}

dragonLoot = ['dragon skin', 'fangs', 'emerald', 'dragon scale']

def addInventory (inventory, addedItems):
    for i in addedItems:
        inventory[i] = random.randint(1,13)

def inventoryCounter (inventory):
    total = 0
    for k, v in inventory.items():
        print (k + ': ' + str(v))
        total += v
    print('The total of items is: ' + str(total))

addInventory(stuff, dragonLoot)
inventoryCounter(stuff)