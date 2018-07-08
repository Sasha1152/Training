inv = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrov':12}
def displayInventory(a):
    for key, value in a.items():
        print(str(value) + ' - ' + str(key))
    print('Total number of items: '),
    print(sum(a.values()))

displayInventory(inv)