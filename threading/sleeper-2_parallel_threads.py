# https://www.youtube.com/watch?v=3u4pa-0mVKU&list=PLV5rPVRE79YikyqHCIrJ33ttjgsXluLVB&index=2

import time
import threading


def sleeper(sec, name):
    print(f'Thread "{name}" go to sleep for {sec} seconds!\n')
    time.sleep(sec)
    print(f'Thread "{name}" woke up!\n')

thread_list = []

for i in ('A', 'B', 'C', 'D'):
    t = threading.Thread(target=sleeper, name=i, args=(3, i))
    thread_list.append(t)
    t.start()
    print(f'Tread "{t.name}" has started')

for t in thread_list:
    t.join()

print('All thread finished!')
