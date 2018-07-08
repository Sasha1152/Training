def add_fruit(inventory, fruit, quantity=0):
    '''
    Adds quantity of fruit to inventory.
    >>> new_inventory = {}
    >>> add_fruit(new_inventory, 'straw', 10)
    >>> new_inventory.has_key('straw')
    True
    >>> new_inventory['straw']
    10
    >>> add_fruit(new_inventory, 'straw', 25)
    >>> new_inventory['straw']
    35
    '''
    if inventory.has_key(fruit):
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
        
            
new_inventory = {}
add_fruit(new_inventory, 'straw', 10)
new_inventory.has_key('straw')
new_inventory['straw']
add_fruit(new_inventory, 'straw', 25)
new_inventory['straw']


if __name__ == '__main__':
    import doctest
    doctest.testmod()
