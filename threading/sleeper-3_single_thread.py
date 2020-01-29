# https://www.youtube.com/watch?v=3u4pa-0mVKU&list=PLV5rPVRE79YikyqHCIrJ33ttjgsXluLVB&index=2

import time


def sleeper(sec, name):
    print(f'Thread "{name}" go to sleep for {sec} seconds!\n')
    time.sleep(sec)
    print(f'Thread "{name}" woke up!\n')


for i in ('A', 'B', 'C', 'D'):
    sleeper(3, i)


print('All thread finished!')
