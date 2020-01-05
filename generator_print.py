def take_ten_elements(iterator):
    a = []
    count = 0
    while count <= 10:
        try:
            a.append(next(iterator))
            count += 1
        except StopIteration:
            break
    return a


generator = (2**i for i in range(32))
print(take_ten_elements(generator))
