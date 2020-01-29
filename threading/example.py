import time
from threading import Thread


def countdown(n):
    for i in range(n):
        print(n - i - 1, "left")
        time.sleep(1.2)

t = Thread(target=countdown, args=(5, ))
t.start()
