# https://hackernoon.com/the-goodies-of-python-decorators-66r3tsy

class FunctionTracker:
    def __init__(self, func):
        self.func = func
        self.stats = []

    def __call__(self, *args, **kwargs):
        try:
            result = self.func(*args, **kwargs)
        except Exception as e:
            self.stats.append((args, kwargs, e))
            # raise e
        else:
            self.stats.append((args, kwargs, result))
            return result

    @classmethod
    def track_function(cls, func):
        return cls(func)


@FunctionTracker.track_function
def func(x, y):
    return x/y

func(4, 2)
func(x=5, y=2)
func(10, y=2)
func(3, 0)
print(func.stats)
print(func)
