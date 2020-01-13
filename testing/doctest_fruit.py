def add_fruit(inventory, fruit, quantity=0):
    """
    Adds quantity of fruit to inventory.
    >>> new_inventory = {}
    >>> add_fruit(new_inventory, 'straw', 10)
    >>> 'straw' in new_inventory
    True
    >>> new_inventory['straw']
    10
    >>> add_fruit(new_inventory, 'straw', 25)
    >>> new_inventory['straw']
    35
    """

    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity



if __name__ == '__main__.py':
    import doctest
    doctest.testmod()
