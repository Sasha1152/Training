class A(object):
    mind = 'yes'
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class B(A):
    def __init__(self, name, surname, age, gender):
        super(B, self).__init__(name, surname)
        self.age = 36
        self.gender = gender

obj_a = A('Kate', 'Rozd')
obj_b = B('Sasha', 'Shmig', 36, 'male')

print(obj_a.name, obj_a.surname)
print(obj_b.name, obj_b.age)
