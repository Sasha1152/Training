# https://stackoverflow.com/questions/189645/how-to-break-out-of-multiple-loops?noredirect=1&lq=1
# https://stackoverflow.com/questions/653509/breaking-out-of-nested-loops?noredirect=1&lq=1


for a in range(5):
    print('a =========== ', a)
    for b in range(4):
        print('b = ', b)
        if a * b > 2:
            # Break the inner loop...
            print('break')
            break

    else:
        # Continue if the inner loop wasn't broken.
        print('continue')
        continue
    # Inner loop was broken, break the outer.
    break