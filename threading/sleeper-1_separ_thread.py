# https://www.youtube.com/watch?v=qM8ZiMOfV98&list=PLV5rPVRE79YikyqHCIrJ33ttjgsXluLVB

import time
import threading


def sleeper(sec, name):
    print(f'Thread "{name}" go to sleep for {sec} seconds!')
    time.sleep(sec)
    print(f'Thread "{name}" woke up!')

t = threading.Thread(target=sleeper, name='Tread-1', args=(3, 'A'))
t.start()
# t.join()
print('Main thread works independently!')

"""
Result without join:
Thread "A" go to sleep for 3 seconds!
Main thread works independently!
Thread "A" woke up!

Result with join:
Thread "A" go to sleep for 3 seconds!
Thread "A" woke up!
Main thread works independently!
"""
