def spam(my_list):
    print(', '.join(my_list[0:-1]) + ' and ' + my_list[-1])
    
spam(['apples', 'bananas', 'tofu', 'cats'])
spam(['one', 'two', 'three', 'four'])
spam(['vodka', 'beer', 'cap of tee'])
