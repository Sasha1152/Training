import time

def power_of(power):
    cache = {}
    def hidden(x):
        start = time.time()
        if x in cache:
            print('Using cached data {} sec'.format(round(time.time() - start, 3)))
            return cache[x]
        else:
            cache[x] = x**power**power
            print('Calculating power of...{} sec'.format(round(time.time() - start, 3)))
            return cache[x]
    return hidden
    
    
p7 = power_of(7)
p7(2)
p7(2)
p7(4)
p7(4)
p7(6)
p7(6)
p7(36)
p7(36)
