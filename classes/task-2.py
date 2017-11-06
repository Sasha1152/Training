""" the task see the book 'Simple Python' - Bill Lubanovich p.178 """

class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    obj_laser = Laser()
    obj_claw = Claw()
    obj_smart = SmartPhone()

    @classmethod
    def does(cls):
        return cls.obj_laser.does(),\
               cls.obj_claw.does(),\
               cls.obj_smart.does()


print(*Robot.does())