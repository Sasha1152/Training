# https://www.youtube.com/watch?v=T7dk-8lSyHE&list=PLV5rPVRE79YikyqHCIrJ33ttjgsXluLVB&index=3

import time
import threading

total = 4

def adding_1():
    global total
    for i in range(6):
        time.sleep(2)
        print(f'adding_1, iteration {i}')
        total += 1
        print('adding_1, iteration finished!')

def adding_2():
    global total
    for i in range(3):
        time.sleep(1)
        print(f'adding_2, iteration {i}')
        total += 1
        print('adding_2, iteration finished!')

def limit_items():
    global total
    while True:
        if total > 5:
            print('overload')
            total -= 3
            print('subtracted by 3')
        else:
            time.sleep(1)
            print('waiting')


adder1 = threading.Thread(target=adding_1)
adder2 = threading.Thread(target=adding_2)
limiter = threading.Thread(target=limit_items, daemon=True)

adder1.start()
adder2.start()
limiter.start()

adder1.join()
adder2.join()
# limiter.join()

print(f'Finished with "total" = {total}')