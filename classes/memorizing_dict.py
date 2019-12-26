class MemorizingDict(dict):
    history = []

    def set(self, key, value):
        self.history.append(key)
        self[key] = value

    def get_history(self):
        return self.history, self


d = MemorizingDict({"foo": 42})
d.set("baz", 100500)
print(d.get_history()) # ['baz']


d = MemorizingDict()
d.set("boo", 500100)
print(d.get_history()) # ['baz', 'boo']
