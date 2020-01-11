########### with property:
class VerySafe:
    def _get_attr(self):
        return self._x

    def _set_attr(self, x):
        assert x > 0, "non-negative value required"
        self._x = x

    def _del_attr(self):
        del self._x

    x = property(_get_attr, _set_attr, _del_attr)

inst = VerySafe()
inst.x = 1
print(inst.x)  # 1

# inst.x = -1  # AssertionError: non-negative value required
print('---' * 3)

################## with descriptor:

class NonNegative:
    def __get__(self, instance, owner):
        # return magically_get_value(...)
        print('"get" method ran')

    def __set__(self, instance, value):
        assert value >= 0, "non-negative value required"
        # magically_set_value(...)
        print('"set" method ran')

    def __delete__(self, instance):
        # magically_delete_value(...)
        return '"delete" method ran'

class VerySafe:
    x = NonNegative()
    y = NonNegative()

very_safe = VerySafe()
very_safe.x = 42  # "set" method ran
very_safe.x  # "get" method ran
del very_safe.x
very_safe.x

# very_safe.y = -1  # AssertionError: non-negative value required
