"""
Метод __call__() автоматически вызывается,
когда к объекту обращаются как к функции
"""

class Changeable:
    def __init__(self, color):
        self.color = color

    def __call__(self, newcolor):
        self.color = newcolor

    def __str__(self):
        return "%s" % self.color


canvas = Changeable("green")
frame = Changeable("blue")
print(canvas, frame)

canvas("red")
frame("yellow")
print(canvas, frame)