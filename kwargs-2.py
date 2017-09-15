def print_kwargs(a = 3, **kwargs):
    print('Keyword arguments:' + str(kwargs))
    print(a)

print_kwargs(wine = 'merlot', entree = 'mutton', dessert = 'macaroon')
print_kwargs(entree = 'mutton', dessert = 'macaroon', a = 'merlot')