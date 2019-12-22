import functools


def once(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            print('wrapper activated')
            func(*args, **kwargs)
            wrapper.called = True
    wrapper.called = False
    return wrapper

@once
def initialize_settings():
    print("Settings initialized.")

initialize_settings()
initialize_settings()
initialize_settings()
initialize_settings()