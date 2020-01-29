import threading
import time

def timeit(f):
    def wrapper(**kwargs):
        started_at = time.time()
        f(**kwargs)
        print('Time: ', time.time() - started_at)
    return wrapper


@timeit
def hendler(started=0, finished=0):
    result = 0
    for i in range(started, finished):
        result += i
    print('Result: ', result)


params = {'started': 1, 'finished': 10**7}

hendler(**params)

task = threading.Thread(target=hendler, kwargs=params)
task.start()
task.join()
