#Chapter 5
#Fantasy Game Inventory

stuff = {'rope': 1, 'torch': 4, 'cheese': 25, 'ham': 10,
         'potions': 19}

def inventoryCounter (inventory):
    total = 0
    print('Would you like add an additional item? (y/n): ', end='')
    response = input()
    if response == 'y':
        print('What is it?: ', end='')
        item = input()
        print('How many?: ', end='')
        quantity = int(input())
        inventory[item] = quantity
    for k, v in inventory.items():
        print (k + ': ' + str(v))
        total += v
    print('The total of items is: ' + str(total))

inventoryCounter(stuff)