class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)


queue = Queue([1, 2, 3])
print(queue)  # Queue([1, 2, 3])
queue.push(0)
print(queue)  # Queue([0, 1, 2, 3])
queue.pop()
print(queue)  # Queue([0, 1, 2])
print(queue._hiddenlist)  # [0, 1, 2]

"""
In the code above, the attribute _hiddenlist is marked as private,
but it can still be accessed in the outside code.
The __repr__ magic method is used for string representation of the instance.
"""